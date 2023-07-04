from typing import Any
from django.contrib.auth.models import User
from .models import RequestLog


class my_middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Initialization")

    
    def __call__(self,request):
        print("This is before view class based Middleware")
        if request.path=="/":
            newentry=RequestLog()
            id=request.user.id
            if id==None:
                newentry.save()
            else:
                userinstance=User.objects.get(id=id)
                newentry.user=userinstance
                newentry.save()
        response = self.get_response(request)
        print("This is after view class based Middleware")
        return response