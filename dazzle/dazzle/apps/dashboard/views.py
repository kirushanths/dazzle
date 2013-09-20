from django.shortcuts import render, get_object_or_404
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

from dazzle.apps.accounts.models import DZUser
from dazzle.apps.dashboard.models import DZSite

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


@login_required
def site_overview(request, site_id):
    site = get_object_or_404(DZSite, pk=site_id)

    context = {
        'site' : site
    }

    return render(request, 'dashboard/overview.html', dictionary=context)
