from rest_framework import serializers
from rest_framework.response import Response

import content
import userProfile
from .models import Shopping_Cart

class ShoppingCartSerializer(serializers.Serializer):

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    item = serializers.PrimaryKeyRelatedField(queryset = content.models.BaseItem.objects.all())
    item_name = serializers.SerializerMethodField('item_name_func')
    quantity = serializers.IntegerField()
    sabad_id = serializers.SerializerMethodField('sabad_id_func')

    def sabad_id_func(self , obj):
        return obj.id

    def item_name_func(self , obj):
        return obj.item.name    

    def create(self , validated_data):

        user = self.context['request'].user
        item = validated_data['item']
        quantity = validated_data['quantity']

        if item.quantity >= quantity:
            user_good = Shopping_Cart.objects.filter(user = user , item = item , status = 'on_cart')
            if len(user_good) == 0:
                user_good = Shopping_Cart.objects.create(user = user , item = item ,  quantity = quantity , status = 'on_cart')
                user_good.save()

            else:
                user_good = user_good[0]
                user_good.quantity += quantity
                user_good.save()

            return user_good

        else:
            raise serializers.ValidationError("There isn't sufficient quantity for this item")

    def update(self , instance , validated_data):

        item = validated_data['item']
        quantity = validated_data['quantity']

        Shopping_Cart.objects.filter(pk = instance.id).update(item = item , quantity = quantity)

        obj = Shopping_Cart.objects.get(pk = instance.id)
        return obj     

class ItemDetail(serializers.ModelSerializer):

    class Meta:
        model = content.models.BaseItem
        fields = ('name' , 'brand' , 'category' , 'price')


class ItemInOrderList(serializers.HyperlinkedModelSerializer):

    detail = serializers.HyperlinkedIdentityField(
        view_name = 'MyOrders-detail',
    )
    class Meta:
        model = Shopping_Cart
        fields = ('detail' , )

class ItemInOrderDetail(serializers.ModelSerializer):
    item = ItemDetail(many = False)
    class Meta:
        model = Shopping_Cart
        fields = ('item' , 'quantity' , 'id')

class Confirmation(serializers.Serializer):

    state_choices = (
        ('accept' , "I accept it , I want to pay for this item") ,
        ('reject' , "I reject it , I want to change something")
    )
    status = serializers.ChoiceField(choices = state_choices)

class Go_To_Confirmation_Step(serializers.Serializer):
    visit_choices = (('action' , 'I want to take an action'),)

    state = serializers.ChoiceField(choices = visit_choices)

class AddressFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    ''' Show addresses that user have '''

    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(AddressFilteredPrimaryKeyRelatedField , self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(information = request.user.users)

class ChooseAddressSerializer(serializers.Serializer):

    state_choices = (
        ('accept' , "I accept it , Go to payment state") ,
        ('reject' , "I reject it , I want to change something")
    )
    status = serializers.ChoiceField(choices = state_choices)
    address = AddressFilteredPrimaryKeyRelatedField(queryset = userProfile.models.UserInformation.objects)

class PayForItem(serializers.ModelSerializer):
    item = ItemDetail(many = False)
    class Meta:
        model = Shopping_Cart
        fields = ('item' , 'quantity')    

class PayConfirmation(serializers.Serializer):

    state_choices = (
        ('accept' , "I accept it , Go to payment state") ,
        ('reject' , "I reject it , I want to change something")
    )
    status = serializers.ChoiceField(choices = state_choices)