from django.http.response import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


def add(req):
    return HttpResponse(json.dumps({'teste':'teste'}))