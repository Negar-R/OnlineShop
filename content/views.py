from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db.models import Q

from datetime import datetime

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

    def get_serializer_class(self):
        return self.serialzers.get(self.action)

class ShowBooks(ReadOnlyModelViewSet):

    queryset = Book.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : BookListSerializer ,
        'retrieve' : BookDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)

class ShowStationeries(ReadOnlyModelViewSet):

    queryset = Stationery.objects.all()

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : StationeryListSerializer ,
        'retrieve' : StationeryDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)

class ShowTopProducts(ReadOnlyModelViewSet):

    queryset = BaseItem.objects.all()

    # def retrieve(self, request, *args, **kwargs):

    #     if instance.category == 'Digital Product':
    #         new_instance = DigitalProduct.objects.get(name = instance.name)
    #     elif instance.category == 'Home Appliance':
    #         new_instance = HomeAppliance.objects.get(name = instance.name)
    #     else:
    #         new_instance = Educational.objects.get(name = instance.name)

    #     serializer = self.get_serializer(new_instance)
    #     return Response(serializer.data)

    print("Before get_serializer")
    def get_serializer_class(self):

        if self.action == 'list':
            # instance = self.get_object()
            # if instance.category == 'Digital Product':
            return MobileListSerializer
        else:
            return TelevisionListSerializer
        return serializers.Default    
        
    print("After get_serializer")


class NewestItems(ReadOnlyModelViewSet):

    Now = datetime.now()
    year = Now.strftime("%Y") 
    year = int(year)
    month = Now.strftime("%m") 
    month = int(month)

    month -= 6
    if month < 1:
        year -= 1
        month = 12 + month

    queryset = BaseItem.objects.filter(created_date = '2020-03-27') 
    serializer_class = RefrigeratorListSerializer
  
