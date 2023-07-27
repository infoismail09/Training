from rest_framework import serializers
from .models import Quotes,Categories

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
