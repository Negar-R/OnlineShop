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


class UserDetail(serializers.ModelSerializer):

    # profile = ProfileDetail(many = False)

    class Meta:
        model = User
        fields = ('username', 'email')

# class FactorDetail(serializers.ModelSerializer):

#     item_name = serializers.SerializerMethodField()

#     def get_item_name(self , item):
#         return item.name

#     class Meta:
#         model = shoppingCart.models.Shopping_Cart
#         fields = ('item_name' , 'status')

class CheckOrdersDetail(serializers.Serializer):

    statue_choices = (
        ('ready' , 'Ready to send') ,
        ('on_process' , 'On Process')
    )
    status = serializers.ChoiceField(choices = statue_choices)


class SuppliarSerializer(serializers.ModelSerializer):
    
    user = UserDetail(many = False)
    item = shoppingCart.serializers.ItemDetail(many = False)

    class Meta:
        model = shoppingCart.models.Shopping_Cart
        fields = ('user' , 'item' , 'quantity' , 'status')

class Suppliar_Factor(serializers.ModelSerializer):

    reciever = ProfileDetail()
    # factor = FactorDetail()
    # factor_detail = serializers.SerializerMethodField()

    # def get_factor_detail(self , suppliar_check_order):
    #     return str(suppliar_check_order.factor.item)
    
    class Meta:
        model = Suppliar_Check_Order
        fields = ('reciever' , 'factor' , 'status')       