from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from api.models import Quotes
from api.serializers import QuotesSerializer

# Create your views here.

@api_view(['GET','POST'])
def quotes_list(request):

    '''
    List of quotes list ,or create new Quotes

    '''
    if request.method == 'GET':
        quotes_data = Quotes.objects.all()
        serializer = QuotesSerializer(quotes_data, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        quotes_serializer = QuotesSerializer(data=request.data)
        print(quotes_serializer)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            msg = {"message":"Data Created Sucessfuly"}
            return Response(msg)
        return Response(quotes_serializer.data)
    
            # Another way to post data using json response.
        #     return JsonResponse(quotes_serializer.data, status=201)
        # return JsonResponse(quotes_serializer.errors, status=400)


@api_view(['GET','PUT','PATCH','DELETE'])


def quotes_details(request,pk):
    if request.method == 'GET':
        quotes_data = Quotes.objects.get(id=pk)
        quotes_serializer= QuotesSerializer(quotes_data)
        return Response(quotes_serializer.data)
    
    elif request.method == "PUT":
        quotes_update = Quotes.objects.get(id=pk)
        quotes_serializer = QuotesSerializer(
            instance = quotes_update, data=request.data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            msg = {"message":"Data Updated Successfully"}
            return Response(msg)
        return Response(quotes_serializer)
    
    elif request.method == 'PATCH':
        quotes_update = Quotes.objects.get(id=pk)
        quotes_serializer = QuotesSerializer(
            instance = quotes_update, data=request.data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            msg = {"message":"Data Partially updated Sucessfully"}
            return Response(msg)
        return Response(quotes_serializer)
    
    elif request.method == 'DELETE':

        quotes_delete = Quotes.objects.filter(id=pk)
        print(quotes_delete)
        if not quotes_delete.exists():
            msg = {"message":"Data Does not exist"}
            return Response(msg) 
        quotes_delete.first().delete()
        msg = {"message":"Data Deleted"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT) 
           
    