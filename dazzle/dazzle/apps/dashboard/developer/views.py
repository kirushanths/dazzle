import urllib2 
import zipfile

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
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseNotAllowed
)
from django.utils import simplejson

from boto import connect_s3
from boto.s3.key import Key  

from dazzle.libs.utils import (
    constants as Constants,
    storage as Storage,
    zipreader
)
from dazzle.apps.accounts.models import DZUser
from dazzle.apps.dashboard.models import DZSite, DZTemplate
from dazzle.apps.dashboard.forms import DZTemplateUploadForm

@login_required
def home(request):
    return HttpResponseRedirect(reverse('developer_manager'))


@login_required
def manager(request):
    if not request.user.is_developer():
        return HttpResponseRedirect(reverse('dashboard_home'))

    user_sites = request.user.sites.all()

    context = {
        'sites': user_sites
    }

    return render(request, 'developer/manager.html', dictionary=context)


@login_required
def upload(request):

    status = None
    if request.POST:
        form = DZTemplateUploadForm(request.POST, request.FILES)

        if form.is_valid():
            template_zipfile = request.FILES.get('template_file')
            template_file_names = []
            template_file_contents = []

            for filename, content in zipreader.fileiterator(template_zipfile):
                template_file_names.append(filename)
                template_file_contents.append(content)

            Storage.s3_upload(
                request.POST.get('template_name'), 
                template_file_names, 
                template_file_contents)
    else:
        form = DZTemplateUploadForm()

    return render(request, 'developer/upload.html', dictionary={ 'form': form })


@login_required
def site_overview(request, site_id=None):
    pass
    #TODO


@login_required
def site_preview(request, site_id=None):
    pass
    #TODO


@login_required
def bank(request):
    pass
    #TODO



