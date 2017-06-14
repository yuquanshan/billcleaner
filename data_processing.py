import django
from billcleaner.splitbill.splitbill import People, billclear
from billcleaner.portal.models import Peep
django.setup()

peeps = Peep.objects.all()

for p in peeps:
	p.actions = ''
	p.save()

fri_group = []
sat_group = []
sun_group = []
mon_group = []

groups = [fri_group, sat_group, sun_group, mon_group]

np = len(peeps)	# number of people

bigtable = []	# record who should pay who
name2n = {}		# name to number in bigtable
number2n = {}	# number to name in bigtable

counter = 0
for p in peeps:
	bigtable.append([0]*np)
	if p.fri:
		fri_group.append(People(str(p.username), p.frimoney))
	if p.sat:
		sat_group.append(People(str(p.username), p.satmoney))
	if p.sun:
		sun_group.append(People(str(p.username), p.sunmoney))
	if p.mon:
		mon_group.append(People(str(p.username), p.monmoney))
	name2n[str(p.username)] = counter 
	number2n[counter] = str(p.username)
	counter += 1

for g in groups:
	smalltable = billclear(g)
	print smalltable
	counter = 0
	for p in g:
		for i in range(0, len(smalltable[counter])):
			if smalltable[counter][i] > 0:
				if counter == i:
					print "ooops!"
				bigtable[name2n[p.name]][name2n[g[i].name]] += \
				smalltable[counter][i]
				bigtable[name2n[g[i].name]][name2n[p.name]] -= \
				smalltable[counter][i]
		counter += 1

print bigtable

for row in range(0,np):
	for col in range(0,np):
		if bigtable[row][col] > 0:
			sender = peeps.get(username=number2n[row])
			receiver = peeps.get(username=number2n[col])
			sender.actions = str(sender.actions) + "You should send ${} to {}. ".format(str(bigtable[row][col]), number2n[col])
			receiver.actions = str(receiver.actions) + "You should receive ${} from {}. ".format(str(bigtable[row][col]), number2n[row])
			sender.save()
			receiver.save()