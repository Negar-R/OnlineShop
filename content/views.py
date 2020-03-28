from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db.models import Q
from django.http import HttpResponse , JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from datetime import datetime , timedelta
import time

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

    queryset = TopProduct.objects.all()
    serializer_class = TopProductSerializer

class ShowAmazingOffers(ReadOnlyModelViewSet):

    queryset = AmazingOffer.objects.all()
    serializer_class = AmazingOfferSerializer

CACHE_TIMEOUT_SECONDS = 30 * 60 * 60 * 24  # this is for 30 days
class NewsetItems(APIView):

    @method_decorator(cache_page(CACHE_TIMEOUT_SECONDS))
    def get(self, request, format = None):
        new_item_ids = []

        one_month_ago = datetime.strftime(datetime.now() - timedelta(days = 30) , "%Y-%m-%d")

        for item in Television.objects.all():
            if str(item.created_date) > one_month_ago:
                new_item_ids.append(item.id)

        new_items = BaseItem.objects.filter(id__in = new_item_ids)

        serializer = NewestItemsSerializer(new_items , many = True)
        return Response(serializer.data)