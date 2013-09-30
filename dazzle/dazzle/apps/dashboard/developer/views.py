import urllib2 

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
from django.utils import simplejson

from boto import connect_s3
from boto.s3.key import Key  

from dazzle.libs.utils import constants as Constants
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
            uploaded_files = request.FILES.getlist('dzfile[]')

            if not uploaded_files:
                return HttpResponseBadRequest

            for f in uploaded_files:
                conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
                bucket = conn.get_bucket(Constants.S3_BUCKET)

                k = Key(bucket)
                k.key = Constants.S3_TEMPLATE_FOLDER + '/' + form.template_name + "/" + f.name
                k.set_acl('public-read')
                k.set_contents_from_file(f) 
        else:
            status = 400

        # TODO get uploaded files
        # TODO get folder name
        # TODO iterate over files into folder

        # TODO: security harderning of uploads
    else:
        form = DZTemplateUploadForm()

    return render(request, 'developer/upload.html', dictionary={ 'form': form }, status=status)


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



