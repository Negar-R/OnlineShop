from rest_framework import serializers
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse

from OnlineShopProject.settings import EMAIL_HOST_USER
from userProfile import models
from suppliar.serializers import FactorDetail
from suppliar.models import Suppliar_Check_Order
import shoppingCart

class SignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 11)
    password1 = serializers.CharField(label='password' , min_length = 4 , max_length = 100 , style = {'input_type' : 'password'})
    password2 = serializers.CharField(label='password confirm' , min_length = 4 , max_length = 100 , style = {'input_type' : 'password'})

    def get_clean_password(self):
        password1 = self.data.get("password1")
        password2 = self.data.get("password2")
        if not password1 or not password2 or password1 != password2:
            raise serializers.ValidationError(('passwords must match'))
        return password2

    def create(self, validated_data):
        clean_password = self.get_clean_password()
        if clean_password:
            user, _ = User.objects.get_or_create(username = validated_data['username'] , email = validated_data['email'])
            user.set_password(clean_password)
            user.save()
            profile, _ = models.UserProfile.objects.get_or_create(user = user , phone = validated_data['phone'])

            subject = 'Verify your QuickPublisher account'
            message = 'Follow this link to verify your account: ''http://localhost:8000%s' % reverse('verify', kwargs = {'uuid': str(profile.verification_uuid)})
            send_mail(subject , message , EMAIL_HOST_USER , [user.email] , fail_silently = False)
            
            return user

    class Meta:
        model = User
        fields = ('username' , 'email' , 'phone' , 'password1', 'password2')
        write_only_fields = ('password1', 'password2')


class UpdateProfileRetrieve(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


class UpdateProfileSerializer(serializers.Serializer):

    username = serializers.CharField(max_length = 200)
    first_name = serializers.CharField(max_length = 200)
    last_name = serializers.CharField(max_length = 200)
    # phone = serializers.CharField(max_length = 200)
    email = serializers.CharField(max_length = 200)
    # cart_number = serializers.CharField(max_length = 19)


class AddressesDetail(serializers.ModelSerializer):
    class Meta:
        model = models.UserInformation
        fields = ('address' ,)

class ShowProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    # address = AddressesDetail(many = True)
    # address = serializers.SerializerMethodField('find_address')

    def get_user(self , user):
        return user.username

    def get_email(self , user):
        return user.email    

    def get_phone(self , user):
        return user.users.phone    

    class Meta:
        model = User
        fields = ('user' , 'email' , 'phone' , 'id')    

class AddAddressSerializer(serializers.Serializer):

    address = serializers.CharField(max_length = 200)
    address_id = serializers.SerializerMethodField('find_address_id')

    def find_address_id(self , obj):
        return obj.id

    def update(self , instance , validated_data):

        address = validated_data['address']

        obj_address = models.UserInformation.objects.filter(pk = instance.id)
        obj_address.update(address = address)

        return obj_address.first()   

class MyShoppingCartList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shoppingCart.models.Shopping_Cart
        fields = ('detail' , )


class MyPaymentedItemSerializer(serializers.ModelSerializer):

    address = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    factor = FactorDetail()

    def get_username(self , suppliar):
        return suppliar.reciever.username

    def get_email(self , suppliar):
        return suppliar.reciever.email 

    def get_address(self , suppliar):
        return suppliar.address.address    

    class Meta:
        model = Suppliar_Check_Order
        fields = ('username' , 'email' , 'phone' , 'address' , 'factor')


class GoToUpdateProfile(serializers.Serializer):

    update_choice = (('I want to update my profile' , 'I want to update my profile') ,)
    profile_update = serializers.ChoiceField(choices = update_choice)