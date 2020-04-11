from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response

from shoppingCart import serializers , models
from userProfile.views import IsVerifiedUser
import suppliar
import userProfile

# Create your views here.


class MyCart(ModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        return models.Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')

    serializer_class = serializers.ShoppingCartSerializer

class MyOrders(ModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        query = models.Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')
        return query   

    serializers = {
        'list' : serializers.ItemInOrderList ,
        'retrieve' : serializers.ItemInOrderDetail ,
        'create' : serializers.Go_To_Confirmation_Step ,
        'update' : serializers.Confirmation,
        'partial_update' : serializers.Confirmation,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action) 

    def create(self , request):
        return Response("Please select an exact debt to confirm or reject it")    

    def update(self , request , *args , **kwargs):
        if request.data['status'] == 'accept':
            obj = models.Shopping_Cart.objects.get(pk = int(kwargs['pk']))
            obj.status = 'ready_to_payed'
            obj.save()
            return Response({'message' : 'مشتری عزیز : وضعیت این جنس در سبد خرید شما به حالت تایید شده درآمد . جنس تایید شده آمده پرداخت میباشد'})

        else :
            obj = models.Shopping_Cart.objects.get(pk = int(kwargs['pk']))
            obj.status = 'on_cart'
            obj.save()
            return Response({'message' : 'We got your response'})   


    def partial_update(self, request, *args, **kwargs):
        return None 


class Payment(ModelViewSet):

    permission_classes = [IsAuthenticated , IsVerifiedUser]

    def get_queryset(self):
        return models.Shopping_Cart.objects.filter(user = self.request.user , status = 'ready_to_payed')

    serializers = {
        'list' : serializers.PayForItem ,
        'create' : serializers.ChooseAddressSerializer,
    }    

    def create(self , request):
        if request.data['status'] == 'accept':
            ordered_item = models.Shopping_Cart.objects.filter(user = self.request.user , status = 'ready_to_payed')
            for ordered in ordered_item:
                ordered.status = ''
                ordered.item.quantity -= ordered.quantity
                ordered.item.save()
                ordered.save()
                profile = userProfile.models.UserProfile.objects.filter(user = self.request.user)
                address = userProfile.models.UserInformation.objects.get(id = self.request.data['address'])
                factors = suppliar.models.Suppliar_Check_Order.objects.create(reciever = self.request.user , phone = profile[0].phone , address = address , factor = ordered)
            return Response({'message' : 'مشتری گرامی ، پرداخت شما با موفقیت انجام شد . به امید دیدار دوباره شما'})
        else:
            return Response({'message' : 'پرداخت شما لغو شد'})    

    def get_serializer_class(self):
        return self.serializers.get(self.action)
