from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from userProfile import serializers , models


class UserSignupApiView(APIView):

    serializer_class = serializers.SignupSerializer

    def post(self, request):
            
        serializer = serializers.SignupSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Your are successfuly singup dear {}'.format(request.data['username'])}) 
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(APIView):

    serializer_class = serializers.UpdateProfileSerializer

    def post(self , request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            address = serializer.validated_data.get('address')
            try:
                user_profile = models.UserProfile.objects.get(user = self.request.user)
            except:
                return Response({'message' : 'You should login first'})
            else:    
                user_info = models.UserInformation.objects.create(address = address)
                user_profile.address.add(user_info)
                user_profile.save()

            return Response({'message' : 'This address has saved for you'})