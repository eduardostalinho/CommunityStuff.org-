from django.conf.urls.defaults import patterns, include, url
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'communitystuff.core.views.welcome'),
    (r'^header', 'communitystuff.core.views.header'),
    (r'^body', 'communitystuff.core.views.body'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'shop/', include(shop_urls)),
)
