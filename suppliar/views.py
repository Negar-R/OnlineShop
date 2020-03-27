from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from suppliar import serializers , models
import shoppingCart

class Factor(ModelViewSet):

    permission_classes = [IsAdminUser]
    queryset = models.Suppliar_Check_Order.objects.filter(status = '')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.Suppliar_Factor
        else:
            return serializers.CheckOrdersDetail    

    def create(self , request):

        if request.data['status'] == 'ready':
            notSended_factors = self.queryset
            for fact in notSended_factors:
                fact.status = 'ready'
                fact.save()
            return Response({'message' : 'All factors sent to contributed part'})
