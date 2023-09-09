from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.

def set_cookie(request):
    response = render(request,'student/setcookie.html')
    # response.set_cookie('username','good coder')  # cookie will avalable till the bowser is open once close it will als destroy automatically
    # response.set_cookie('username','good coder',max_age=60 ) #max_age = 60 sec we use for how log cookie wil be visible after 60 sec automatically delete
    # response.set_cookie('username','good coder',expires=datetime.utcnow()+timedelta(days=2)) # it will expire after 2 days even if browser close also.
    response.set_cookie('username','Bottle') # we change value of cookie
    return response

def get_cookie(request):
    # mydata = request.COOKIES['username']   # after delete if we run this it wil trow errors
    # mydata = request.COOKIES.get('username') # it will show none
    mydata = request.COOKIES.get('username','No cookie Available') # it will show no data available
    return render(request,'student/getcookie.html',{'mydata':mydata})


def delete_Custom_cookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie('username')
    return response

