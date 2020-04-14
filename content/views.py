from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.reverse import NoReverseMatch, reverse

from django.db.models import Q
from django.http import HttpResponse , JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from datetime import datetime , timedelta
from collections import OrderedDict
import time

from .models import *
from .serializers import *
from shoppingCart import serializers

class APIRootView(APIView):

    _ignore_model_permissions = True
    schema = None  # exclude from schema
    api_root_dict = None

    def get(self, request, *args, **kwargs):
        # Return a plain {"name": "hyperlink"} response.
        ret = OrderedDict()
        namespace = request.resolver_match.namespace
        for key, url_name in self.api_root_dict.items():
            if namespace:
                url_name = namespace + ':' + url_name
            try:
                ret[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get('format', None)
                )
            except NoReverseMatch:
                # Don't bail out if eg. no list routes exist, only detail routes.
                continue
        
        list_of_categories = []
        dict1_of_categories = {}
        dict2_of_categories = {}
        dict3_of_categories = {}

        dict1_of_categories['Home_appliance'] = [{'Refrigerator' : ret['Refrigerator']} , {'TV' : ret['TV']}]
        dict2_of_categories['Digital_Products'] = [{'Laptob' : ret['Laptob']} , {'Mobile' : ret['Mobile']}]
        dict3_of_categories['Educational'] = [{'Book' : ret['Book']} , {'Stationery' : ret['Stationery']}]

        list_of_categories.append(dict1_of_categories)
        list_of_categories.append(dict2_of_categories)
        list_of_categories.append(dict3_of_categories)

        return Response(list_of_categories)


class ShowRefrigerators(ReadOnlyModelViewSet):

    queryset = Refrigerator.objects.all()

    lookup_field = 'slug'

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

    lookup_field = 'slug'

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

    lookup_field = 'slug'

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

    lookup_field = 'slug'

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

    lookup_field = 'slug'

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

    lookup_field = 'slug'

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

        for item in BaseItem.objects.all():
            if str(item.created_date) > one_month_ago:
                new_item_ids.append(item.id)

        new_items = BaseItem.objects.filter(id__in = new_item_ids)

        serializer = NewestItemsSerializer(new_items , many = True)
        return Response(serializer.data)