from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,HttpRequest,HttpResponseBadRequest,JsonResponse
from .models import User
import simplejson
import jwt
import datetime
import bcrypt
# Create your views here.
AUTH_EXPIRE = 8*60*60
def authenticate(view):
    def wrapper(request:HttpRequest):
        payload = request.META.get('HTTP_COOKIE')
        if not payload:
            return HttpResponse(status=401)
        try:
            payload = payload.lstrip('JWT=')
            payload = jwt.decode(payload, settings.SECRET_KEY, algorithms='HS256')
            print(payload)
        except Exception as e:
            print(e)
            return HttpResponse(status=401)
        # current = datetime.datetime.now().timestamp()
        # if(current - payload.get('timestamp',0) > AUTH_EXPIRE):
        #     return HttpResponse(status=401)
        try:
            user_id = payload.get('user_id',-1)
            user = User.objects.filter(id = user_id).get()
            request.user = user
        except:
            return HttpResponse(status=401)

        ret = view(request)
        return ret
    return wrapper
def gen_token(userid):
    return jwt.encode({
        'user_id' : userid,
        'exp' : int(datetime.datetime.now().timestamp())+AUTH_EXPIRE,
    },key= settings.SECRET_KEY,algorithm='HS256').decode()
def reg(request:HttpRequest):
    payload = simplejson.loads(request.body)
    try:
        name = payload['name']
        email = payload['email']
        password = bcrypt.hashpw(payload['password'].encode(),bcrypt.gensalt())
        query = User.objects.filter(email = email)
        print(query)
        if query:
            return HttpResponseBadRequest()
        user = User()
        user.name = name
        user.email = email
        user.password = password
        try:
            user.save()
            return JsonResponse({"token":gen_token(user.id)})
        except:
            raise
    except Exception as e:
        return HttpResponseBadRequest
def login(request:HttpRequest):
    payload = simplejson.loads(request.body)
    try:
        email = payload['email']
        password = payload['password']
        user = User.objects.filter(email=email).get()
        if bcrypt.checkpw(password.encode(),user.password.strip('b \'').encode()):
            token = gen_token(user.id)
            res = JsonResponse({
                'user' :{
                    'user.name' : user.name,
                    'user.email' : user.email,
                    'user.id' : user.id
                }, 'token' : token
            })
            res.set_cookie('JWT',token)
            return res
        return HttpResponseBadRequest(status=401)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()
