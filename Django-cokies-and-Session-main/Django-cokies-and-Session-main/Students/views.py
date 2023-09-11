from django.shortcuts import render, HttpResponse

# Create your views here.


def set_cookie(request):
    response = render(request, "Students/setcookie.html")
    response.set_cookie(
        "username", "good coder"
    )  # max_age = 120 we use for how log cookie wil be visible
    return response


def get_cookie(request):
    # mydata = request.COOKIES['username']
    mydata = request.COOKIES.get("username", "No cookie data")
    return render(request, "Students/getcookie.html", {"mydata": mydata})


def delete_Custom_cookie(request):
    response = render(request, "Students/deletecookie.html")
    response.delete_cookie("username")
    return response


def create_session(request):
    request.session["data"] = {
        "name": "Ismail",
        "age": 24,
        "height": 5.4,
    }
    request.session["password"] = "alpha123"
    return HttpResponse("Session data is Set")


def access_session(request):
    response = "Welcome to session"
    if request.session.get("data"):
        response += "Name is {0}".format(request.session.get("data"))

    if request.session.get("password"):
        response += "pasword is {0}".format(request.session.get("password"))
        return HttpResponse(response)

    else:
        return HttpResponse("No Session data")


def delete_session(request):
    try:
        del request.session["data"]
        del request.session["password"]
    except KeyError:
        return HttpResponse("No Session data")

    return HttpResponse("Session Data Cleared")
