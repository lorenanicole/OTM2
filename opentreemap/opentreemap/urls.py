from django.conf.urls import patterns, include, url
from example.views import index


from django.contrib import admin
admin.autodiscover()

from treemap.views import index, settings

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'opentreemap.views.home', name='home'),
    # url(r'^opentreemap/', include('opentreemap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^config/settings.js$', settings)
)