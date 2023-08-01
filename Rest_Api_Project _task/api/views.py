from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from api.models import Quotes,Categories,Products
from api.serializers import QuotesSerializer,CategoriesSerializer,ProductSerializer
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
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# below i mport is for Session Autentication
from rest_framework.authentication import SessionAuthentication


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

@extend_schema(request=QuotesSerializer,responses=QuotesSerializer)
@api_view(['GET','PUT','PATCH','DELETE'])
def quotes_details(request,pk):
# GET Functionality
    if request.method == 'GET':
        quotes_data = Quotes.objects.get(id=pk)
        quotes_serializer= QuotesSerializer(quotes_data)
        return Response(quotes_serializer.data)
    
# PUT Functionality 
    elif request.method == "PUT":
        quotes_update = Quotes.objects.get(id=pk)
        quotes_serializer = QuotesSerializer(
            instance = quotes_update, data=request.data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            msg = {"message":"Data Updated Successfully"}
            return Response(msg)
        return Response(quotes_serializer)
    
# PATCH Functionality

    elif request.method == 'PATCH':
        quotes_update = Quotes.objects.get(id=pk)
        quotes_serializer = QuotesSerializer(
            instance = quotes_update, data=request.data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            msg = {"message":"Data Partially updated Sucessfully"}
            return Response(msg)
        return Response(quotes_serializer)
    
 # DELETE Functionality
    elif request.method == 'DELETE':
        quotes_delete = Quotes.objects.filter(id=pk)
        print(quotes_delete)
        if not quotes_delete.exists():
            msg = {"message":"Data Does not exist"}
            return Response(msg) 
        quotes_delete.first().delete()
        msg = {"message":"Data Deleted"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT) 
    

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
#     # filter_backends = [SearchFilter]
#     # search_fields = ['title']
#     # filterset_fields  = ['title','created at'] # example for multiple feilds
#     search_fields = ['^title'] 
    # search_fields = ['=title']  # Exact Serch
    # search_fields = ['@title']  # full search
    # search_fields = ['$title']  # regex serch


############ Implementing Ordering Filter ########################

# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [OrderingFilter]
#     ordering_fields  = ['created_at']


############### Implementing check list last task of search and filter that is for search for both product and category

class Category_list(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

class ProductList(ListAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [SearchFilter]
    search_fields = ['title']   

################## Now implementing Generics API View ####################

# for listing All product list  Using Generics Concrete Api View

# class ProductList(ListAPIView):   
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     # pagination_class = MyPageNumberPagination    # numberpagination   
#     # pagination_class = MyCursorPagination           # Cursor Pagination
#     pagination_class = MyLimitOffsetPagination

# Creat APi View
class ProductCreate(CreateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer 

# Retrieve API View # use to fetch individual or single data using id 
class ProductRetrieve(RetrieveAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer   

# Update API view
class ProductUpdate(UpdateAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer  

# Delete API View
class ProductDelete(DestroyAPIView):   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

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

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

