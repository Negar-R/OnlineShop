from rest_framework import serializers
from rest_framework.response import Response

from django.contrib.auth.models import User

from userProfile import models

class SignupSerializer(serializers.Serializer):
    
    username = serializers.CharField(min_length = 4 , max_length = 200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 11)
    password = serializers.CharField(min_length = 4 , max_length = 100 , style = {'input_type' : 'password'})

class UpdateProfileSerializer(serializers.Serializer):
    
    address = serializers.CharField(max_length = 200)