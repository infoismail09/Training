from django.shortcuts import render
from django.http import HttpResponse
from . models import Musician,Album
# Create your views here.

def get_musician(requests):
    # details = Musician.objects.all()
    # details = Musician.objects.get(pk=1) # The get() method is used to retrieve a single object that matches the specified filter criteria. It returns the actual model instance, not a queryset. Since it returns a single instance, there is no need for a query to be constructed, and therefore, there is no query attribute associated with it. 
    details = Musician.objects.filter(pk=1) #  The filter() method is used to create a queryset that represents a collection of objects that match the specified filter criteria. It does not retrieve the objects immediately; instead, it constructs a query that will be executed when the queryset is evaluated. You can inspect the SQL query by accessing the query
    details = Musician.objects.filter(intrument="piano")
    details = Musician.objects.exclude(last_name="singh")
    print(details.query)
    return HttpResponse(
        "<h1>Welcome to My Object Relational Mapping <br>Musician</br></h1>"
    )
