import copy

class People:
	def __init__(self, name, money):
		self.name = name
		self.money = float(money)
		self.defi = 0.0
		self.suffi = 0.0

class Bag:
	def __init__(self, size, tag):
		self.tag = tag
		self.left = size
		self.balls = []	# the balls people have

class Baginstance:
	def __init__(self):	# n is number of bags
		self.count = 0
		self.bags = []
	def addBag(self,bag):
		self.bags.append(bag)

def packbags(balls, baginst):
	bestsofar = baginst
	if len(balls) > 0:
		s = balls.pop(0)
		for i in range(0,len(baginst.bags)):
			if baginst.bags[i].left >= s.defi:
				"""
					it might be a memory-consuming approach, alternatively, we 
					can use a user-to-bag matrix plus a bag-left-capacity array
					to record the mapping, and just copy the matrix and array
				"""
				temp = copy.deepcopy(baginst)
				temp.bags[i].left -= s.defi
				temp.bags[i].balls.append(s)
				temp.count += 1
				tmp = packbags(balls, temp)
				if tmp.count > bestsofar.count:
					bestsofar = tmp
		temp = copy.deepcopy(baginst)
		tmp = packbags(balls, temp)
		if tmp.count > bestsofar.count:
			bestsofar = tmp
	return bestsofar

def billclear(people):
	s = 0
	for p in people:
		s += p.money
	avg = s/len(people)
	binst = Baginstance()
	owers = []
	owners = []
	for p in people:
		if avg >= p.money:
			p.defi = avg - p.money
			owers.append(p)
		else:
			p.sufi = p.money - avg
			binst.bags.append(Bag(p.sufi, p.name))
			owners.append(p)
	table = []
	for p in people:
		table.append([0]*len(people))
	pton = {}	# name to number mapper
	name2p = {}	# name to people mapper
	counter = 0
	for p in people:
		pton[p.name] = counter
		name2p[p.name] = p
		counter += 1
	res = packbags(copy.copy(owers), binst)
	clearset = set()
	for bag in res.bags:
		for p in bag.balls:
			clearset.add(p.name)
			table[pton[p.name]][pton[bag.tag]] = p.defi
			name2p[bag.tag].sufi -= p.defi
			clearset.add(p.name)
	for ower in owers:
		if ower.name not in clearset:
			while(len(owners) > 0):
				if owners[0].sufi >= ower.defi:
					owners[0].sufi -= ower.defi
					table[pton[ower.name]][pton[owners[0].name]] += ower.defi
					ower.defi = 0
					break
				else:
					table[pton[ower.name]][pton[owners[0].name]] += \
					owners[0].sufi

					ower.defi -= owners[0].sufi
					owners[0].sufi = 0
					owners.pop(0)
	return table


def renderres(table, people):
	counter = 0
	for p in people:
		for i in range(0,len(table[counter])):
			if table[counter][i] > 0:
				print "{} should pay {} ${}".format(p.name,people[i].name,
					table[counter][i])
		counter += 1

"""
a = People("Amy", 3)
b = People("Bob", 0)
c = People("Charlie", 50.5)
d = People("David", 26.8)
e = People("Eve", 270.77)
f = People("Frank",88)

people = [a,b,c,d,e,f]
t = billclear(people)
#print t
renderres(t,people)
"""

"""
a = People("Amy", 3)
a.defi = 3
b = People("Bob", 5)
b.defi = 5
c = People("Charlie", 3)
c.defi = 3
d = People("David", 3)
d.defi = 3
e = People("Eve", 6)
e.defi = 6

bag1 = Bag(9, "bag1")
bag2 = Bag(1, "bag2")
bag3 = Bag(4, "bag3")
bag4 = Bag(4, "bag4")
bag5 = Bag(2, "bag5")

bi = Baginstance()
bi.addBag(bag1)
bi.addBag(bag2)
bi.addBag(bag3)
bi.addBag(bag4)
bi.addBag(bag5)

bags = packbags([a,b,c,d,e], bi)
for i in bags.bags:
	print i.tag+":"
	for j in i.balls:
		print "   "+j.name
"""