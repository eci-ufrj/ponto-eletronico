from django.http.response import HttpResponse
from utils.json_utils import json_view

# Create your views here.

@json_view
def add_user(request):
    pass

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
