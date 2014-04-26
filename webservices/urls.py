from django.conf.urls import patterns, url
from .views import add_user

urlpatterns = patterns('',
    # Examples:
    url(r'^add_user/$', add_user, name='adduser'),
    url(r'^place/add_place/$', 'add_place', name='addplace'),
    url(r'^timecard/add_starttime/$', 'add_starttime', name='add'),
    url(r'^timecard/add_endtime/$', 'add_endtime', name='add2'),
)

