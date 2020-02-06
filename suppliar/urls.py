from django.urls import path , include

from rest_framework.routers import DefaultRouter

from suppliar import views

router = DefaultRouter()
router.register('Factors' , views.Admin_Ordered)
# router.register('new' , views.Factor)

urlpatterns = [
    path('idiot' , include(router.urls))
]
