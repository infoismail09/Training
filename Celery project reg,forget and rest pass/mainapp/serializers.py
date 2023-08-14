from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
