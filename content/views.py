from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *
from shoppingCart import serializers

class ShowRefrigerators(ReadOnlyModelViewSet):

    queryset = Refrigerator.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : RefrigeratorListSerializer ,
        'retrieve' : RefrigeratorDetailSerilizer
    }
    
    def get_serializer_class(self):
        return self.serialzers.get(self.action)


class ShowTelevisions(ReadOnlyModelViewSet):

    queryset = Television.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : TelevisionListSerializer ,
        'retrieve' : TelevisionDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)


class ShowLaptobs(ReadOnlyModelViewSet):

    queryset = Laptob.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : LaptobListSerializer ,
        'retrieve' : LaptobDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)


class ShowMobiles(ReadOnlyModelViewSet):

    queryset = Mobile.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : MobileListSerializer ,
        'retrieve' : MobileDetailSerilizer
    }

    # @action(detail = True , methods = ['create'] , permission_classes = [])
    # def add_to_shopping_cart(self , request):
    #     serializer_class = serializers.ShoppingCartSerializer

    #     serializer = self.serializer_class(data = request.data)
        
    #     if serializer.is_valid():
    #         return Response('WOoOOw')

    def get_serializer_class(self):
        return self.serialzers.get(self.action)