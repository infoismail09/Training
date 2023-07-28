from rest_framework import serializers
from .models import Quotes,Categories,Products

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'text', 'created_at' , 'updated_at']
        read_only_fields =  ['id' ,'created_at' , 'updated_at']  #this field we have to take when we dont want to send all feild s data so that post method can work properly


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        read_only_fields =  ['created_at' , 'updated_at'] 
        depth = 1

class ProductSerializer(serializers.ModelSerializer):
    product = CategoriesSerializer(many=True,read_only=True) #this line is ued to work for nested serializer 
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields =  ['created_at' , 'updated_at','product'] # included what to show in the nested serializer in the fields 
        depth = 1



