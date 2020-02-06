from django.urls import path , include

from rest_framework.routers import DefaultRouter

from shoppingCart import views

router = DefaultRouter()

router.register('MyShoppingCart' , views.MyCart , basename = 'MyShoppingCart')
router.register('MyOrders' , views.MyOrders , basename = 'MyOrders')

urlpatterns = [
    path('finance/' , include(router.urls)),
]
