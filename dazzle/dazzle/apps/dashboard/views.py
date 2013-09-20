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
    return HttpResponseRedirect(reverse('apps.dashboard.views.manager'))

@login_required
def manager(request):

    # get user
    try:
        user = DZUser.objects.filter(email = request.user.email)
    except DZUser.DoesNotExist:
        return HttpResponse("Invalid email")

    print(request.user.sites.all())

    return render(request, 'dashboard/manager.html')    