from rest_framework import generics
from django.db.models import Q
from .models import Product
from . import serializers


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    search_fields = ("title", "category__title")

    def get_queryset(self):
        qs = Product.objects.all()
        query_params = self.request.GET

        # search = query_params.get("search")

        title = query_params.get("title")


        # q_object = Q()
        # if search:
        #     for field in self.search_fields:
        #         q_object.add(Q(**{f"{field}__icontains": search}), Q.AND)
        #     qs = qs.filter(q_object)

        if title:
            qs = qs.filter(title__icontains=title)
        return qs
