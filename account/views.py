from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from account import forms,models

# Create your views here.

def user_register(request , *args, **kwargs):

	if request.method == 'POST':
		registered =False
		form = forms.UserForm(data=request.POST)
		if form.is_valid():
			form.save(commit=True)
			registered =True
			messages.success(request,'Account Successfully Created!')
			return redirect('login')
			
		else:

			messages.error(request,'Unable To Save Form!')
	else:

		form = forms.UserForm()

	context={'form':form}
	return render(request,'account/register.html',context)


def user_login(request, *args, **kwargs):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			models.User.objects.get(username=username)
		except:
			messages.error(request,'User Not Exist!')
		else:
			
			user = authenticate(request,username=username,password=password)

			if user is not None:

				login(request,user)
				return redirect('dashboard')

			else:

				messages.error(request,'Username And Password Is Not Valid')
	context={}
	return render(request,'account/login.html',context)


def user_logout(request):

	logout(request)
	return redirect('home')