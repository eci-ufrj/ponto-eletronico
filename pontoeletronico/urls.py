from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pontoeletronico.views.home', name='home'),
    url(r'^ws/', include('webservices.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
