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
		fields = ['fri', 'frimoney', 'sat', 'satmoney', 'sun', 'sunmoney', 'mon', 'monmoney']
		labels = {
			'fri': 'Friday (Bowling)',
			'frimoney': 'Friday Expense',
			'sat': 'Saturday (Monterey)',
			'satmoney': 'Saturday Expense',
			'sun': 'Sunday (Hearst Castle etc)',
			'sunmoney': 'Sunday Expense',
			'mon': 'Monday (Santa Barbara etc)',
			'monmoney': 'Monday Expense',
		}
		help_texts = {
			'fri': 'Click if you participated',
			'sat': 'Click if you participated',
			'sun': 'Click if you participated',
			'mon': 'Click if you participated',
		}
