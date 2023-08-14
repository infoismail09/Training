from django.shortcuts import render
from mainapp.task import  send_reset_password_link, send_change_password_email,send_generate_password_link
from mainapp.form import CreateUserForm
from django.shortcuts import render
from django.contrib.auth.models import User
from mainapp.serializers import RegisterUserSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == "GET":
        user = User.objects.all()
        user_serializer = RegisterUserSerializers(user, many=True)
        return Response(user_serializer.data)

    elif request.method == "POST":
        email = request.data['email']
        # password = request.data['password']
        # request.data['password'] = make_password(password)
        user_serializer = RegisterUserSerializers(data=request.data)
        # print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            send_generate_password_link.delay(email)
            return JsonResponse(user_serializer.data)

@csrf_exempt
def generate_password(request):
    email = request.GET.get('email')
    password = request.POST.get('password')
    user = User.objects.get(email=email)

    password = make_password(password)
    print(password)
    user.password = password
    user.set_password(password)
    user.save()
    return JsonResponse({"msg": "password change succesfully"})

# @api_view(['GET', 'POST'])
# def register_user(request):
#     if request.method == "GET":
#         user = User.objects.all()
#         user_serializer = RegisterUserSerializers(user, many=True)
#         return Response(user_serializer.data)

#     elif request.method == "POST":
#         email = request.data['email']
#         password = request.data['password']
#         request.data['password'] = make_password(password)
#         user_serializer = RegisterUserSerializers(data=request.data)
#         # print(user_serializer)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             send_mail_after_register.delay(email)
#             return JsonResponse(user_serializer.data)


@api_view(['GET', 'POST'])
def reset_password_link(request):
    email = request.GET.get('email')
    user = User.objects.get(email=email)
    send_reset_password_link.delay(email)
    return Response("sent")


@csrf_exempt
def change_password(request):
    email = request.GET.get('email')
    password = request.POST.get('password')
    user = User.objects.get(email=email)

    password = make_password(password)
    user.password = password
    user.save()
    send_change_password_email.delay(email)
    return JsonResponse({"msg": "password change succesfully"})


# def signup_mail(request):

#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             send_mail_after_register.delay()
#     return render(request, 'register.html', {'form': form})


# def send_mail_to_all(request):
#     send_mail_to_all.delay()
#     return HttpResponse("Sent Succesfully")
