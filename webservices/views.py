from django.http.response import HttpResponse
import json


# Create your views here.


def addPerson(req):
    return HttpResponse(json.dumps({'teste':'teste'}))