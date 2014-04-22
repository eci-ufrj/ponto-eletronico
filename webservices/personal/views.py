from backend.pessoal.api import addPerson, getPeople, setPersonAsBoss
from backend.pessoal.models import Person
from django.http.response import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render
from utils.json_utils import json_view

# Create your views here.

@json_view
def addBoss(req):
    if req.method != "POST":
        return HttpResponse(u"Only POST is supported.", status=405)
    name = req.POST.get('name', None)
    if name:
        return addPerson(name)
    else:
        return HttpResponseForbidden()

@json_view
def addWorker(req):
    if req.method != "POST":
        return HttpResponse(u"Only POST is supported.", status=405)
    name = req.POST.get('name', None)
    if name:
        return addPerson(name)
    else:
        return HttpResponseForbidden()

@json_view
def getPeopleWS(req):
    return getPeople()

@json_view
def setBossWS(req):
    id = req.GET.get('id', None)
    if id:
        return setPersonAsBoss(id)
    else:
        return HttpResponseForbidden()