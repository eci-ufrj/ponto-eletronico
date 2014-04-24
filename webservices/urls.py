from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^/user/add_user/$', 'add_user', 'add user'),
    url(r'^/place/add_place/$', 'add_place', 'add place'),
    url(r'^/timecard/add_starttime/$', 'add_starttime', 'add'),
    url(r'^/timecard/add_endtime/$', 'add_endtime', 'add')
)

