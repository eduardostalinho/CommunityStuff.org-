from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'communitystuff.core.views.welcome'),
    url(r'header', 'communitystuff.core.views.header'),
    url(r'body', 'communitystuff.core.views.body'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
