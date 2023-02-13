from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection
from web import models
import base64
from utils.encrypt import md5
from utils.generate_image import generate_code
import re
from utils.ajax_response import BaseResponse
from io import BytesIO
from web.forms.account import RegisterForm


#
# from web.forms.account import LoginForm, mobileLoginForm, MobileForm
def varify(account, password):
    return True


def login(request):
    user = None
    if request.method == 'GET':
        return render(request, 'login.html')
    response = BaseResponse()
    res = request.POST
    if res.get('code') and res.get('mobile'):
        response, user = login_with_code(request)
    elif res.get('account') and res.get('password'):
        response, user = login_with_password(request)

    # passed all validations
    if response.success:
        request.session['user_id'] = user.id
        request.session['user_type'] = user.user_type
        request.session['user_name'] = user.username
        request.session['level'] = user.level_id

    return JsonResponse(response.dict)


def login_with_code(request):
    user = None
    res = request.POST
    response = BaseResponse()
    try:
        mobile = base64.b64decode(res.get('mobile')).decode()
        code = base64.b64decode(res.get('code')).decode()
    except:
        response.message = 'Mobile phone number or verification code format error'
        return response, user
    # Check if the user exists in the database
    user = models.User.objects.filter(mobile=mobile, active=1).first()
    if not user:
        response.message = 'User does not exist'
        return response, user
    # Check whether the verification code is correct
    redis_conn = get_redis_connection('default')
    redis_code = redis_conn.get(mobile)
    if not redis_code:
        response.message = 'verification code has expired'
        return response, user
    if redis_code != code:
        response.message = 'verification code error'
        return response, user
    # login success
    response.success = True
    response.message = 'login success'
    return response, user


def login_with_password(request):
    user = None
    res = request.POST
    response = BaseResponse()
    try:
        account = base64.b64decode(res.get('account')).decode()
        password = base64.b64decode(res.get('password')).decode()
    except:
        response.message = 'account or password format error'
        return response, user
    # Determine whether the account passed in is a mobile phone number or an email address
    phone_regex = re.compile(r'^04[0-9]{8}$')
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if phone_regex.match(account):
        mobile = account
        user = models.User.objects.filter(mobile=mobile, active=1, password=md5(password)).first()
    elif email_regex.match(account):
        username = account
        user = models.User.objects.filter(username=username, active=1, password=md5(password)).first()
    else:
        response.message = 'account or password format error'
        return response, user
    # Check if the user exists in the database
    if not user:
        response.message = 'user does not exist'
        return response, user
    # Login success
    response.message = 'login success'
    response.success = True
    return response, user


def get_code(request):
    print(request.POST)
    response = BaseResponse()
    try:
        mobile = base64.b64decode(request.POST.get('mobile')).decode()
    except:
        response.message = 'the mobile format is wrong'
        return JsonResponse(response.dict)

    # Determine whether the mobile phone number has sent a verification code
    redis_conn = get_redis_connection('default')
    cache_code = redis_conn.get(mobile)
    if cache_code:
        response.message = 'the code is already sent, please wait for 60 seconds'
        return JsonResponse(response.dict)

    # Determine whether the mobile phone number is registered
    exists = models.User.objects.filter(mobile=mobile).exists()
    if exists:
        sms_code = '123456'
        sms_success = True
        if not sms_success:
            response.message = 'message send failed'
            return JsonResponse(response.dict)
    else:
        response.message = 'the mobile is not registered'
        return JsonResponse(response.dict)

    redis_conn.set(mobile, sms_code, ex=60)
    response.success = True
    return JsonResponse(response.dict)


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    form = RegisterForm(data=request.POST)
    if not form.is_valid():
        return render(request, "register.html", {"form": form})

    # Create a user
    username = form.cleaned_data.pop('username')
    password = form.cleaned_data.pop('password_repeat')

    user = models.User.objects.create(username=username, password=password)
    # write to session
    request.session['user_id'] = user.id
    request.session['user_type'] = user.user_type
    request.session['user_name'] = user.username
    request.session['level'] = user.level_id
    return redirect('/index/')


def logout(request):
    request.session.clear()
    return redirect('/')


def index(request):
    return HttpResponse('here is index')

def home(request):
    return render(request, 'home.html')

def image_question(request):
    # Generate questions
    img = generate_code()
    # Return the image
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue(), content_type='image/png')
