from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseBadRequest,JsonResponse,HttpResponseNotFound
from .models import Post,Content
from users.models import User
import simplejson
import datetime
import math
from users.views import authenticate
# Create your views here.
@authenticate
def pub(request:HttpRequest):
    post = Post()
    content = Content()
    try:
        payload = simplejson.loads(request.body)
        post.title = payload['title']
        post.author = User(id = request.user.id)
        post.postdate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.save()
        content.content = payload['content']
        content.title = post
        content.save()
        return JsonResponse({"post.id":post.id})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest
def get(request:HttpRequest,id):
    print(id)
    try:
        id = int(id)
        post = Post.objects.get(id = id)
        if post:
            return JsonResponse({
                'post':{
                'post_id' : post.id,
                'title' : post.title,
                'datetime' : post.postdate.timestamp(),
                'author_id' : post.author.id,
                'author' : post.author,
                'content' : post.content.content


            }})
    except Exception as e:
        print(e)
        return HttpResponseNotFound()
def validate(d:dict,name:str,type_func,default,validate_func):
    try:
        result = type_func(d.get(name,default))
        result = validate_func(result,default)
    except:
        result = default
    return result
def getall(request:HttpRequest):
    page = validate(request.GET,'page',int,1,lambda x,y:x if x>0 else 1)
    size = validate(request.GET,'size',int,20,lambda x,y:x if x>0 and x<101 else y)
    try:
        print('***',request.body)
        start = (page - 1)*size
        posts = Post.objects.order_by('-id')
        print(posts.query)
        count = posts.count()

        posts = posts[start:start +size]
        print('***',posts.query)
        print(posts,'123')
        return JsonResponse({
            'posts':[
                {
                    'post_id':post.id,
                    'title':post.title
                } for post in posts
            ],'pagination':{
                'page':page,
                'size':size,
                'count':count,
                'pages':math.celi(count/size)

            }
        })
    except Exception as e:
        return HttpResponseBadRequest()

