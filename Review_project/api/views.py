from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Company,Branch
from api.serializers import CompanySerializer,BranchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@extend_schema(responses=CompanySerializer,request=CompanySerializer)
@api_view(['GET', 'POST'])
def company_list(request):
    #  List all company, or create a new compa
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
 
    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 

class CompaniesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


 
