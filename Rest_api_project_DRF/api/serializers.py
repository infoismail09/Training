from rest_framework import serializers
from django.contrib.auth.models import user

class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = (
            'id',
            'text',
            'created_at',
            'updated_at',
        )



