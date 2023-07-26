from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def myview(request):
    return HttpResponse('<h1>Function based view</h2>')

# class bsaed view
class Myview(View):
    name = 'Ismail'
    def get(self,request):
            # return HttpResponse('<h1>Class based view -GET </h2>')
        return HttpResponse(self.name)
    
class MyViewChild(Myview):
    def get(self,request):
        return HttpResponse(self.name)


