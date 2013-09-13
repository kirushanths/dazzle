# Create your views here.
from django.shortcuts import render
from django.contrib.auth import (
	authenticate as django_auth
	login as django_login
	logout as django_logout
)

def home(request):
    return render(request, 'core/home.html')

def login(request):
	username = request.POST['username']
    password = request.POST['password']
    user = django_auth(username=username, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.

	return render(request, 'core/login.html')

def logout(request):
    django_logout(request)
    # Redirect to a success page.

def register(request):
	return render(request, 'core/register.html')