from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^personal/', include('webservices.personal.urls'))
)

