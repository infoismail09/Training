from django.shortcuts import render
from  django.http import HttpResponse  
from django.template.response import TemplateResponse

# Create your views here.

# def home(request):
#     print("I am view")
#     return HttpResponse("This is Home Page")

######### same  view for class based also 

# def home(request):
#     print("I am view")
#     return HttpResponse("This is Home Page")


####### reating view for an exception ############

def home(request):
    print(" I Am Home view")
    return HttpResponse("This is Home Page")

# def excp(request):
#     print(" I Am Excp view")
#     a = 10/0
#     return HttpResponse("This is Excp Page")

def user_info(request):
    print(" I Am User Info view")
    context  = {'name':'Ismail'}
    return TemplateResponse(request, 'blog/simple.html',context)