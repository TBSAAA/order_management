from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection
from web import models


from utils.ajax_response import BaseResponse
#
# from web.forms.account import LoginForm, mobileLoginForm, MobileForm


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    print(request.POST)
    response = BaseResponse()
    try:
        response.detail = request.POST
    except Exception as e:
        response.status = False
        response.code = str(e)
    return JsonResponse(response.dict)


def get_code(request):
    print(request.POST)
    return JsonResponse({'status': True, 'code': '1234'})


def register(request):
    pass


def logout(request):
    pass


def index(request):
    pass
