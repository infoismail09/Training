from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .models import *
# Create your views here.

def home(request):
    payload = []
    db = None
    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
        print(cache.ttl('fruits'))  # use of ttl is that it will indicate in terminal kitne time baad cache expire hoga
    else:
        objs = Fruits.objects.all()
        for obj in objs:
            payload.append(obj.fruit_name)
        db = 'sqllite'
        cache.set('fruits', payload,timeout=10) # we can give time that kitne seconds baad cache expire hoga .
    return JsonResponse({'status': 200, 'db': db, 'data': payload})
