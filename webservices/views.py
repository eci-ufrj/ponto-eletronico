from db.api import addUser
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from utils.json_utils import json_view
import demjson as json

# Create your views here.

@csrf_exempt
@json_view
def add_user(request):
    data = {}
    try:
        params = json.decode(request.body)
    except Exception as ex:
        data['success'] = False
        data['error_msg'] = u"A user or a username must be set in the body of the request, as a json. E.g.: {name: Joao, username:joazinho}"
        return data, 200
    if not params.get('name') or  not params.get('username'):
        data['success'] = False
        data['error_msg'] = u"A user or a username must be set."
        return data, 405
    return addUser(**params)

@json_view
def add_place(request):
    pass

@json_view
def add_starttime(request):
    pass

@json_view
def add_endtime(request):
    pass

@json_view
def get_users(request):
    pass
