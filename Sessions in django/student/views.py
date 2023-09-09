from django.shortcuts import render

# Create your views here.

# def setsession(request):
#     request.session['name'] = 'Sabir'
#     request.session['lname'] = 'Shaikh'
#     return render(request,'student/setsession.html')


# def getsession(request):
#     # name = request.session['name']
#     # name = request.session.get('name',default='Guest')
#     # lname = request.session.get('lname',default='Guest')
#     name = request.session.get('name')
#     keys = request.session.keys()
#     items = request.session.items()
#     # age = request.session.setdefault('age','26')  # ye set bhi karta and get bhi karta hai
#     # return render(request,'student/getsession.html',{'name':name,'lname':lname})
#     return render(request,'student/getsession.html',{'name':name,'keys':keys})
#     # return render(request,'student/getsession.html',{'name':name,'items':items,'age':age})


# # def delsession(request):
# #     if 'name' in request.session:
# #         del request.session['name']
# #     return render(request,'student/delsession.html')

# # for flush
# def delsession(request):
#     request.session.flush
#     return render(request,'student/delsession.html')


##### Methods in sesssion ##############


def setsession(request):
    request.session['name'] = 'Saurabh'
    # request.session.set_expiry(10)  # giving time for expiring session
    return render(request,'student/setsession.html')


def getsession(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,'student/getsession.html',{'name':name})


def delsession(request):
    request.session.flush
    request.session.Clear_expired()
    return render(request,'student/delsession.html')


########## Test Cookies ###############


def settestcookies(request):
    request.session.set_test_cookie()
    return render(request,'student/settestcookie.html')


def checktestcookies(request):
    request.session.test_cookie_worked()
    return render(request,'student/checktestcookie.html')


def deltestcookies(request):
    request.session.delete_test_cookie()
    return render(request,'student/deltestcookie.html')
