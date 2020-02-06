from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from suppliar import serializers , models
import shoppingCart
# Create your views here.

class Admin_Ordered(ModelViewSet):

    # permission_classes = [IsAdminUser]
    queryset = shoppingCart.models.Shopping_Cart.objects.filter(status = 'payed')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SuppliarSerializer
        else:
            return serializers.CheckOrdersDetail


# class Factor(ModelViewSet):

#     # permission_classes = [IsAdminUser]
#     queryset = models.Suppliar_Check_Order.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.Suppliar_Factor
#         else:
#             return serializers.CheckOrdersDetail    