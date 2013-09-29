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

from boto import connect_s3
from boto.s3.key import Key  

from dazzle.apps.accounts.models import DZUser
from dazzle.apps.dashboard.models import DZSite, DZTemplate
from dazzle.libs.utils import constants as Constants

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

    if request.POST:

        # TODO get uploaded files
        # TODO get folder name
        # TODO iterate over files into folder

        # TODO: security harderning of uploads

        conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
        bucket = conn.get_bucket(Constants.S3_BUCKET)

        k = Key(bucket)
        k.key = Constants.S3_TEMPLATE_FOLDER + '/' + template_name + "/" + file.name
        k.set_acl('public-read')
        k.set_contents_from_file(file)

    return render(request, 'developer/upload.html')


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



