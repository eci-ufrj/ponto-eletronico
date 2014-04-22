from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^add/$', 'webservices.personal.views.addPersonWS', name='add'),
    url(r'^get/$', 'webservices.personal.views.getPeopleWS', name='get'),
    url(r'^setBoss/$', 'webservices.personal.views.setBossWS', name='addBoss'),
    
)

