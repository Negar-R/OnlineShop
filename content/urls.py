from django.urls import path , include

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.views import SchemaView
from rest_framework.settings import api_settings
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

from collections import OrderedDict
from django.conf.urls import url



class Router(DefaultRouter):
  
    APIRootView = APIRootView
  
    def get_api_root_view(self, api_urls=None):
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)

router = Router()

router.register('Refrigerator' , ShowRefrigerators)
router.register('TV' , ShowTelevisions)
router.register('Laptob' , ShowLaptobs)
router.register('Mobile' , ShowMobiles)
router.register('Book' , ShowBooks)
router.register('Stationery' , ShowStationeries)


urlpatterns = [
    path('menu/' , include(router.urls)),
    path('new_items' , NewsetItems.as_view()),
    path('Amazing_Offers' , ShowAmazingOffers.as_view({'get' : 'list'})),
    path('Top_Products' , ShowTopProducts.as_view({'get' : 'list'}))
]