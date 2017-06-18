from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Peep
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
	class Meta:
		model = Peep
		fields = ['username', 'password1', 'password2']

class ReportForm(ModelForm):
	class Meta:
		model = Peep
		fields = ['fri', 'frimoney', 'sat', 'satmoney', 'sun', 'sunmoney', 
		'mon', 'monmoney', 'sat1', 'sat1money', 'sun1', 'sun1money']
		labels = {
			'fri': 'Friday (Bowling)',
			'frimoney': 'Friday Expense',
			'sat': 'Saturday (Monterey)',
			'satmoney': 'Saturday Expense',
			'sun': 'Sunday (Hearst Castle etc)',
			'sunmoney': 'Sunday Expense',
			'mon': 'Monday (Santa Barbara etc)',
			'monmoney': 'Monday Expense',
			'sat1': 'Saturday (San Jose Night Bar)',
			'sat1money': 'Another Saturday Expense',
			'sun1': 'Sunday (San Jose Daytime)',
			'sun1money': 'Another Sunday Expense',
		}
		help_texts = {
			'fri': 'Click if you participated',
			'sat': 'Click if you participated',
			'sun': 'Click if you participated',
			'mon': 'Click if you participated',
			'sat1': 'Click if you participated',
			'sun1': 'Click if you participated',
		}
