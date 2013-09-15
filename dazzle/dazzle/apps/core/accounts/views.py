from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'core/home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = django_auth(username=username, password=password)

        if user is not None:
            if user.is_active:
                django_login(request, user)
                return HttpResponseRedirect(reverse('apps.core.dashboard.views.home'))
            else:
                # Return a 'disabled account' error message
                print('asdf')
        else:
            # Return an 'invalid login' error message.
            print('asdf')

    return render(request, 'core/accounts/login.html')

def logout(request):
    django_logout(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('apps.core.accounts.views.login'))

def register(request):
    return render(request, 'core/accounts/register.html')