from rest_framework import serializers

from django.contrib.auth.models import User 

import userProfile
import shoppingCart
from .models import Suppliar_Check_Order

class ProfileDetail(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self , profile):
        return profile.user.username

    def get_email(self , profile):
        return profile.user.email  

    class Meta:
        model = userProfile.models.UserProfile
        fields = ('username' , 'email' , 'phone' , 'address')

class FactorDetail(serializers.ModelSerializer):

    item = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    def get_item(self , shopping_cart):
        return shopping_cart.item.name

    def get_quantity(self , shopping_cart):
        return shopping_cart.quantity       

    class Meta:
        model = shoppingCart.models.Shopping_Cart
        fields = ('item' , 'quantity')

class CheckOrdersDetail(serializers.Serializer):

    statue_choices = (
        ('ready' , 'Ready to send') ,
        ('on_process' , 'On Process')
    )
    status = serializers.ChoiceField(choices = statue_choices)

class Suppliar_Factor(serializers.ModelSerializer):

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