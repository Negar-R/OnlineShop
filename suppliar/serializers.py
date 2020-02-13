from rest_framework import serializers

from django.contrib.auth.models import User 

import userProfile
import shoppingCart
from .models import Suppliar_Check_Order

class ProfileDetail(serializers.ModelSerializer):
    class Meta:
        model = userProfile.models.UserProfile
        fields = ('phone' , 'address')


class UserDetail(serializers.ModelSerializer):

    # profile = ProfileDetail(many = False)

    class Meta:
        model = User
        fields = ('username', 'email')


class CheckOrdersDetail(serializers.Serializer):

    statue_choices = (
        ('ready' , 'Ready to send') ,
        ('on_process' , 'On Process')
    )
    status = serializers.ChoiceField(choices = statue_choices)


class SuppliarSerializer(serializers.ModelSerializer):
    
    user = UserDetail(many = False)
    # CheckOrders = CheckOrdersDetail(many = False)
    item = shoppingCart.serializers.ItemDetail(many = False)

    class Meta:
        model = shoppingCart.models.Shopping_Cart
        fields = ('user' , 'item' , 'quantity' , 'status')

class Suppliar_Factor(serializers.ModelSerializer):

    reciever = ProfileDetail()
    
    class Meta:
        model = Suppliar_Check_Order
        fields = ('reciever' , 'factor' , 'status')       