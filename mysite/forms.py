from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	User.objects.username = forms.CharField(label='Username', max_length=100)


	class Meta:
    	model = User
    	fields = ['username']