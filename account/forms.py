from account import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

	class Meta():
		model = models.User
		fields=['name','username','email','password1','password2','avatar']

	 