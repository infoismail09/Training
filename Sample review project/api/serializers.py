from rest_framework import serializers
from api import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "title"
        )

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = models.Product
        fields = (
            "id",
            "title",
            "category"
        )