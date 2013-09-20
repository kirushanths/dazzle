from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import DZUserModelForm

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = django_auth(username=username, password=password)

        if user is not None:
            if user.is_active:
                django_login(request, user)
                return HttpResponseRedirect(reverse('apps.dashboard.views.home'))
            else:
                # Return a 'disabled account' error message
                print('asdf')
        else:
            # Return an 'invalid login' error message.
            print('asdf')

    return render(request, 'accounts/login.html')

def logout(request):
    django_logout(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('apps.accounts.views.login'))

def register(request):
    if request.POST:
        user_form = DZUserModelForm(request.POST)
        if user_form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            dzuser = user_form.save(commit=False)
            dzuser.save()
            #redirect
            return HttpResponseRedirect(reverse('apps.dashboard.views.home'))
        else:
            print('error')
            #failed
    else:
        user_form = DZUserModelForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})

