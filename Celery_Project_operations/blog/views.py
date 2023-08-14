from django.shortcuts import render
from blog.tasks import send_reset_password_link
from django.http import HttpResponse
# Create your views here.


def Reset_password_link(request):
    send_reset_password_link.delay()
    return HttpResponse("LinkSend")


