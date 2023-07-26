from django.shortcuts import render
from django.core.cache import cache

# Create your views here.

# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','The manjhi',30)
#         mv = cache.get('movie')
#     return render(request,'enroll/home.html',{'fm':mv})


# def home(request):
#     mv = cache.get_or_set('fees',200,30, version=2)
#     return render(request,'enroll/home.html',{'fm':mv})

# def home(request):
#     data = {'name':'Ismail','roll':101}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request,'enroll/home.html',{'stu': sv})

# def home(request):
#     cache.delete('name')
#     return render(request,'enroll/home.html')  # delete cache


# def home(request):
#     cache.set('roll',101,60)
#     rv = cache.get('roll')
#     print(rv)
#     return render(request,'enroll/home.html') # example to add roll no in cache anow below we are decresing valuve of roll 


# def home(request):
#     dv = cache.decr('roll',delta=1)
#     print(dv)
#     return render(request,'enroll/home.html') # cache decrement value of a feild


# def home(request):
#     dv = cache.incr('roll',delta=2)
#     print(dv)
#     return render(request,'enroll/home.html') # cache increment value by 2


## clear all cache ##

def home(request):
    cache.clear()
    return render(request,'enroll/home.html')