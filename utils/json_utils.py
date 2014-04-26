'''
Created on 22/04/2014

@author: submarino
'''
from django.http import HttpResponse
import demjson as json


def json_view(func):
    def wrap(req, *args, **kwargs):

        resp = func(req, *args, **kwargs)

        if isinstance(resp, HttpResponse):
            return resp
        
        try:
            resp, status = resp[0],resp[1]
        except:
            resp, status = resp, None

        return HttpResponse(json.encode(resp), status=status)

    return wrap