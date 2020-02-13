from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response

from shoppingCart import serializers , models
import suppliar
import userProfile

# Create your views here.


class MyCart(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = models.Shopping_Cart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer

class MyOrders(ModelViewSet):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print("***********" , self.request.user)
        return models.Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')


    def get_serializer_class(self):

        if self.action == 'list':    
            return serializers.ItemInOrder
        else:
            return serializers.Confirmation    


    def create(self , request):

        if request.data['Final_state'] == 'accept':
            
            ordered_item = models.Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')
            for ordered in ordered_item:
                ordered.status = 'payed'
                print(ordered.item.quantity)
                ordered.item.quantity -= ordered.quantity
                ordered.item.save()
                ordered.save()
                print("***" , ordered.item.quantity)
                profile = userProfile.models.UserProfile.objects.filter(user = self.request.user)
                print("&&&&" , profile[0])
                factors = suppliar.models.Suppliar_Check_Order.objects.create(reciever = profile[0])
                print(ordered.item.id)
                print(ordered.item.name)
                print("@@@@ ORDERED : " , ordered)
                factors.factor.add(ordered)
                factors.save()
                print("$$$$$$$$$$$$")
            return Response({'message' : 'مشترک گرامی ، پرداخت شما با موفقیت انجام شد . به امید دیدار دوباره شما'})

        else :
            return Response({'message' : 'We got your response'})    


