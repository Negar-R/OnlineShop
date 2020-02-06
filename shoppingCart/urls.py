from django.urls import path , include

from rest_framework.routers import DefaultRouter

from shoppingCart import views

router = DefaultRouter()

router.register('MySabad' , views.SabadKharid)
router.register('MyOrders' , views.MyOrders , basename = 'MyOrders')

urlpatterns = [
    path('finance' , include(router.urls)),
    path('sabadddd' , views.SabadKharid.as_view({'get' : 'list' , 'post' : 'create'}))
]
