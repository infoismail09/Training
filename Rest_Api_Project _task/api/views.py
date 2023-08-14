from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from api.models import Quotes,Categories,Products,FAQs
from api.serializers import QuotesSerializer,CategoriesSerializer,ProductSerializer,FaqsSerializer
from drf_spectacular.utils import extend_schema
from .mypaginations import MyPageNumberPagination
# from .mypaginations import MyCursorPagination
from .mypaginations import MyLimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# from rest_framework.generics import CreateAPIView
# Below import is for basic authentication implementation 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# below i mport is for Session Autentication
from rest_framework.authentication import SessionAuthentication
# below custom permission import
from .custompermissions import MyPermission
# below token Autentication imported
from rest_framework.authentication import TokenAuthentication
# from api.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# importing for thortling 
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import JackRateThrottle
# for alag alag part of api appling throttle
from rest_framework.throttling import ScopedRateThrottle


@extend_schema(request=QuotesSerializer,responses=QuotesSerializer)
@api_view(['GET','POST'])
def quotes_list(request):

    '''
    List of quotes list ,or create new Quote
    '''
    
    if request.method == 'GET':
        # quotes_data = Quotes.objects.all()
        # serializer = QuotesSerializer(quotes_data, many=True)
        # return Response(serializer.data)

        quotes_data = Quotes.objects.all()
        qoutes_filter = request.query_params.get("filter")
        if qoutes_filter != None:
            quotes_data = Quotes.objects.filter(text=qoutes_filter)
        paginator = MyPageNumberPagination()
        result_page = paginator.paginate_queryset(quotes_data, request)

        serializer = QuotesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


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

# @extend_schema(request=QuotesSerializer,responses=QuotesSerializer)
# @api_view(['GET','PUT','PATCH','DELETE'])
# def quotes_details(request,pk):
# # GET Functionality
#     if request.method == 'GET':
#         quotes_data = Quotes.objects.get(id=pk)
#         quotes_serializer= QuotesSerializer(quotes_data)
#         return Response(quotes_serializer.data)
    
# # PUT Functionality 
#     elif request.method == "PUT":
#         quotes_update = Quotes.objects.get(id=pk)
#         quotes_serializer = QuotesSerializer(
#             instance = quotes_update, data=request.data)
#         if quotes_serializer.is_valid():
#             quotes_serializer.save()
#             msg = {"message":"Data Updated Successfully"}
#             return Response(msg)
#         return Response(quotes_serializer)
    
# # PATCH Functionality

#     elif request.method == 'PATCH':
#         quotes_update = Quotes.objects.get(id=pk)
#         quotes_serializer = QuotesSerializer(
#             instance = quotes_update, data=request.data)
#         if quotes_serializer.is_valid():
#             quotes_serializer.save()
#             msg = {"message":"Data Partially updated Sucessfully"}
#             return Response(msg)
#         return Response(quotes_serializer)
    
#  # DELETE Functionality
#     elif request.method == 'DELETE':
#         quotes_delete = Quotes.objects.filter(id=pk)
#         print(quotes_delete)
#         if not quotes_delete.exists():
#             msg = {"message":"Data Does not exist"}
#             return Response(msg) 
#         quotes_delete.first().delete()
#         msg = {"message":"Data Deleted"}
#         return Response(msg,status=status.HTTP_204_NO_CONTENT) 
    

############# Now Creating Class Based view For Categories ##############


class Categories_List(APIView):
    '''
    List all Categories detail and create a new category
    '''
    @extend_schema(responses=CategoriesSerializer)
    def get(self,request):
        # categiories_data = Categories.objects.all()
        # serializer = CategoriesSerializer(categiories_data, many=True)
        # return Response(serializer.data)

        category_data = Categories.objects.all()
        category_filter = request.query_params.get("filter")
        if category_filter != None:
            category_data = Categories.objects.filter(title=category_filter)
        paginator = MyPageNumberPagination()
        result_page = paginator.paginate_queryset(category_data, request)

        serializer = CategoriesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    
    @extend_schema(request=CategoriesSerializer,responses=CategoriesSerializer)
    def post(self,request, format= None):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Categories_details(APIView):

    '''
    Retrieve , Update or Delete a Categories

    '''
    @extend_schema(responses=CategoriesSerializer)
    def get_object(self,pk):
        try:
            return Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        Categories_data = self.get_object(pk)
        serializer = CategoriesSerializer(Categories_data)
        return Response(serializer.data)
    
    @extend_schema(request=CategoriesSerializer,responses=CategoriesSerializer)
    def put(self,request,pk):
        categories_update = self.get_object(pk)
        serializer = CategoriesSerializer(categories_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = {"message":"Data updated Sucessfully"}
            return Response(msg)
        return Response(serializer.data)
    
    @extend_schema(responses=CategoriesSerializer)
    def delete(self,request,pk):
        categories_delete = self.get_object(pk)
        categories_delete.delete()
        msg = {"message":"Data Deleted Sucessfully"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)        



############### Implementing Filter and search functionality


# normal filter using filter orm
# class Category_list(ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Categories.objects.filter()

#  generics filter backend 
# using filter backed doing * per view filter and for globally implemented in setting .py

# class Category_list(ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields  = ['title']
#     # filterset_fields  = ['title','created at'] # example for multiple feilds

############### Implementing serch filter functionality 

# class Category_list(ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['title']
#     filterset_fields  = ['title','created at'] # example for multiple feilds
#     search_fields = ['^title'] 
#     search_fields = ['=title']  # Exact Serch
#     search_fields = ['@title']  # full search
#     search_fields = ['$title']  # regex serch


############ Implementing Ordering Filter ########################

# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [OrderingFilter]
#     ordering_fields  = ['created_at']


############### Implementing check list last task of search and filter that is for search for both product and category

# class Category_list(ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['title']

# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer 
#     filter_backends = [SearchFilter]
#     search_fields = ['title']   

################## Now implementing Generics API View ####################

# for listing All product list  Using Generics Concrete Api View

# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     # pagination_class = MyPageNumberPagination    # numberpagination   
#     # pagination_class = MyCursorPagination           # Cursor Pagination
#     pagination_class = MyLimitOffsetPagination

# # list of all products
# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# # Creat APi View
# class ProductCreate(CreateAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer 

# # Retrieve API View # use to fetch individual or single data using id 
# class ProductRetrieve(RetrieveAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer   

# # Update API view
# class ProductUpdate(UpdateAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer  

# # Delete API View
# class ProductDelete(DestroyAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
    

# now implementing generics concrete API view combination 

#listing and creating data 
class ProductListCreate(ListCreateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Retrive and update Api view combo
class ProductRetriveUpdate(RetrieveUpdateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Retrieve and Destroy Api view
class ProductRetriveDestroy(RetrieveDestroyAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Retrive update and destroy
class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


######### Viewset in class based view for nested serializer concept ##############

# class CategoriesViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer


# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer


########## basic Authentication and permission class ###############
# this is for individual class view if global go to settings and configure

# class CategoriesViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [IsAdminUser]  # is will access by only admin user only who stats is ids staff true.

# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]    # if we dont want to authenticate particular view simple implement AllowAny and import also 
#                                       # we can over ride global by using AllowAny


############### Implementing session Authentication ##############

# class CategoriesViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()

#     serializer_class = CategoriesSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated] # isme check karega wo login hai ya nahi nahi hai toh login karna padhega
    # permission_classes = [IsAdminUser]   # isme jiska staff status tick rahega wo access kar payega
    # permission_classes = [AllowAny]    # if we dont want to authenticate particular view simple implement AllowAny and import also 
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Agar register user hai to post update and delete kar payega and anony mous user hai toh sirif api get kar sakta hai
    # permission_classes = [DjangoModelPermissions]  # isme authentication compulsory hai and poat man se test karenge toh csrf token chiye hog operation perforn karne ke liye
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # isme jo authnticate  hoga wo sirif read kar payega get but moddel permission bhi llagegi put ,post and delete ke liye
    

############## Implementing Custom Permissions ##################

# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [MyPermission]


############ Implementing Autentication and permisiion in Function based view ################

# @extend_schema(request=QuotesSerializer,responses=QuotesSerializer)
# @api_view(['GET','PUT','PATCH','DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])

# def quotes_details(request,pk):
# # GET Functionality
#     if request.method == 'GET':
#         quotes_data = Quotes.objects.get(id=pk)
#         quotes_serializer= QuotesSerializer(quotes_data)
#         return Response(quotes_serializer.data)
    
# # PUT Functionality 
#     elif request.method == "PUT":
#         quotes_update = Quotes.objects.get(id=pk)
#         quotes_serializer = QuotesSerializer(
#             instance = quotes_update, data=request.data)
#         if quotes_serializer.is_valid():
#             quotes_serializer.save()
#             msg = {"message":"Data Updated Successfully"}
#             return Response(msg)
#         return Response(quotes_serializer)
    
# # PATCH Functionality

#     elif request.method == 'PATCH':
#         quotes_update = Quotes.objects.get(id=pk)
#         quotes_serializer = QuotesSerializer(
#             instance = quotes_update, data=request.data)
#         if quotes_serializer.is_valid():
#             quotes_serializer.save()
#             msg = {"message":"Data Partially updated Sucessfully"}
#             return Response(msg)
#         return Response(quotes_serializer)
    
#  # DELETE Functionality
#     elif request.method == 'DELETE':
#         quotes_delete = Quotes.objects.filter(id=pk)
#         print(quotes_delete)
#         if not quotes_delete.exists():
#             msg = {"message":"Data Does not exist"}
#             return Response(msg) 
#         quotes_delete.first().delete()
#         msg = {"message":"Data Deleted"}
#         return Response(msg,status=status.HTTP_204_NO_CONTENT) 
           

############# Implementing Token Autentication ###############

# 1) we can generate token with cmd line in terminal by simpley typing 
# python manage.py drf_create_token username (e.g vedant)
# Generated token 83fd2e81063725d07da694348aa21b60625f3d1e for user vedant
# note agar phele se hoga token toh mil jayega wahi token

# 2) we can generate token by migrate and then from admin with the help of rest_framework.authtoken

# 3) we can generate through httpie we have to congigure in main project url obtain_auth_token then create 1 end point then in terminal intall httpie
# then type http POST http:http://127.0.0.1:8000/gettoken/username="vedant" password="django2023" 

# Point to note down 
#beow for GET
# http://127.0.0.1:8000/viewset/categories/ 'Authorization: Token 870f90d048a3c51b244ec7b706a3c94153a7b722 with use of abbove line interminal we can see data in terminal

# below for POST
# http -f POST http://127.0.0.1:8000/viewset/categories/ title='mongo' 'Authorization: Token 870f90d048a3c51b244ec7b706a3c94153a7b722 with use of abbove line interminal we can see data in terminal

#below for PUT
# http PUT http://127.0.0.1:8000/viewset/categories/4 title='Apphanso' 'Authorization: Token 870f90d048a3c51b244ec7b706a3c94153a7b722 with use of abbove line interminal we can see data in terminal


# class CategoriesViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Agar register user hai to post update and delete kar payega and anony mous user hai toh sirif api get kar sakta hai


########## Implementing Custom Authentication #########################


# by using username we can use api
# http://127.0.0.1:8000/viewset/categories/?username=admin
# http://127.0.0.1:8000/viewset/categories/1/?username=admin

# class CategoriesViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     authentication_classes = [CustomAuthentication]
#     permission_classes = [IsAuthenticated]



######### Implementation of Json Web Token (JWT) #############


# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]


# # Creat APi View
# class ProductCreate(CreateAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated] 

# # Retrieve API View # use to fetch individual or single data using id 
# class ProductRetrieve(RetrieveAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer 
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]  

# # Update API view
# class ProductUpdate(UpdateAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer 
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated] 

# # Delete API View
# class ProductDelete(DestroyAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]


########### Implementing FAQS View for File upload and for casching ################

class FaqsListCreate(ListCreateAPIView):
    queryset = FAQs.objects.all()
    serializer_class = FaqsSerializer
    
    @method_decorator(cache_page(1800)) # for 30 mintues cache
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RetrieveUpdateDestroyFaqs(RetrieveUpdateDestroyAPIView):
    queryset = FAQs.objects.all()
    serializer_class = FaqsSerializer


############## now implementing Thtottling concept ##################


# # list of all products
# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # throttle_classes = [AnonRateThrottle,UserRateThrottle]
#     # throttle_classes = [AnonRateThrottle,JackRateThrottle] # customize throttle 

#  thorttling diffrent concept for api ke alag alag part ko hum trottle kar sakte hai

# list of all products
class ProductList(ListAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewpro'

# Creat APi View
class ProductCreate(CreateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer 
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modipro'

# Retrieve API View # use to fetch individual or single data using id 
class ProductRetrieve(RetrieveAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]   # isko hum globally bhi kar sakte hai settings me 
    throttle_scope = 'viewpro'   #random string
    

# Update API view
class ProductUpdate(UpdateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer 
    throttle_classes = [ScopedRateThrottle] 
    throttle_scope = 'modipro'

# Delete API View
class ProductDelete(DestroyAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modipro'
    



