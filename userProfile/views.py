from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.db.models import signals
from django.core.mail import send_mail
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken , JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer


from userProfile import serializers , models
import shoppingCart , suppliar


class IsVerifiedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print("@@@@@@@@@@@" , request.user)
        return request.user.users.is_verified


class UserSignupApiView(APIView):

    serializer_class = serializers.SignupSerializer

    def post(self, request):
            
        serializer = serializers.SignupSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Your are successfuly singup dear {}'.format(request.data['username'])}) 
        return Response(serializer.errors , status = status.HTTP_401_UNAUTHORIZED)


class UpdateProfileView(ModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        return User.objects.filter(username = self.request.user.username)

    serializer = {
        'list' : serializers.ShowProfileSerializer ,
        'retrieve' : serializers.UpdateProfileSerializer,
        'create' : serializers.GoToUpdateProfile,
        'update' : serializers.UpdateProfileSerializer,
        'partial_update' : serializers.UpdateProfileSerializer,
    }    

    def create(self , request):
        return Response({'message' : 'Please enter you id at the end of your url to update your profile'})

    def update(self , request, *args, **kwargs):

        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']

        user_obj = User.objects.get(pk = int(kwargs['pk']))
        user_obj.username = username
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.email = email
        user_obj.save()

        return Response({'message' : 'Your profile was updated dear {0} {1}'.format(first_name , last_name)})    

    def partial_update(self, request, *args, **kwargs):
        return None

    def destroy(self, request, *args, **kwargs):
        return Response("You do not have permission to delete your profile")

    def get_serializer_class(self):
        return self.serializer.get(self.action)
          

class AddAddressView(ModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        return models.UserInformation.objects.filter(information = self.request.user.users)

    serializer_class = serializers.AddAddressSerializer

    def create(self , request):

        user_profile = models.UserProfile.objects.get(user = self.request.user)
        user_info = models.UserInformation.objects.create(address = request.data['address'])
        user_profile.address.add(user_info)
        user_profile.save()

        return Response({'message' : 'This address has saved for you'})   


class ShowMyShoppingCartView(ReadOnlyModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]
    
    def get_queryset(self):
        return shoppingCart.models.Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')

    serializer = {
        'list' : serializers.MyShoppingCartList,
        'retrieve' : shoppingCart.serializers.ItemInOrderDetail
    }  

    def get_serializer_class(self):
        return self.serializer.get(self.action)


class ShowMyPaymentedItems(ReadOnlyModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        return suppliar.models.Suppliar_Check_Order.objects.filter(reciever = self.request.user)

    serializer_class = serializers.MyPaymentedItemSerializer


def verify(request, uuid):
    try:
        user = models.UserProfile.objects.get(verification_uuid = uuid, is_verified = False)
    except:
        raise Http404("User does not exist or is already verified")
 
    user.is_verified = True
    user.save()

    return redirect('http://127.0.0.1:8000/login/')