from django.urls import path , include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('Refrigerator' , ShowRefrigerators)
router.register('TV' , ShowTelevisions)
router.register('Laptob' , ShowLaptobs)
router.register('Mobile' , ShowMobiles)
router.register('Book' , ShowBooks)
router.register('Stationery' , ShowStationeries)
router.register('Top_Products' , ShowTopProducts)
router.register('Amazing_Offers' , ShowAmazingOffers)


urlpatterns = [
    path('menu/' , include(router.urls)),
    path('new_items' , NewsetItems.as_view()),
]
