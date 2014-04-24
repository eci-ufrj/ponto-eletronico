'''
Created on 22/04/2014

@author: submarino
'''
import json

from django.http import HttpResponse

def json_view(func):
    def wrap(req, *args, **kwargs):

        resp = func(req, *args, **kwargs)

        if isinstance(resp, HttpResponse):
            return resp

        return HttpResponse(json.dumps(resp), content_type="application/json")

    return wrap