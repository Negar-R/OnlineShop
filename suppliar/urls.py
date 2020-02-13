from django.urls import path , include

from rest_framework.routers import DefaultRouter

from suppliar import views

router = DefaultRouter()
router.register('old' , views.Admin_Ordered)
router.register('Factors' , views.Factor)

urlpatterns = [
    path('suppliar/' , include(router.urls))
]
