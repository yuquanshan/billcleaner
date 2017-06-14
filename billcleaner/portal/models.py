# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Peep(User):
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)
	sun = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	frimoney = models.FloatField(default=0.0)
	satmoney = models.FloatField(default=0.0)
	sunmoney = models.FloatField(default=0.0)
	monmoney = models.FloatField(default=0.0)
	comment = models.CharField(max_length=100, default="")
	actions = models.CharField(max_length=1000, 
		default="Submit expense report and wait for admin to close the case")
	
	"""def get_money(self):
		money = []
		days = ['Fri','Sat','Sun','Mon']
		counter = 0
		for f in self._meta.fields:
			value = getattr(self, name)
			money.append(
				{
					'label': days[counter],
					'value': str(value),
				}
			)
			counter += 1
		return money
	"""