from django.http import HttpResponse
from django.shortcuts import redirect


def index(resquest):
    return HttpResponse

def login(request):
    return redirect('/index')
