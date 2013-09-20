from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)

from dazzle.apps.accounts.models.user import DZUser

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def manager(request):

    # get user
    try:
        dzuser = DZUser.objects.get(username = request.user).select_related(depth=1)
    except DZUser.DoesNotExist:
        return HttpResponse("Invalid username")

    print (dzuser)

    return render(request, 'dashboard/manager.html')    