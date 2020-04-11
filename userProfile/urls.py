from django.urls import path , include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.routers import DefaultRouter

from userProfile import views

router = DefaultRouter()
router.register('update_profile' , views.UpdateProfileView , basename = 'userprofile')
router.register('add_address' , views.AddAddressView , basename = 'userinformation')
router.register('my_shopping_cart' , views.ShowMyShoppingCartView , basename = 'shopping_cart')
router.register('my_paymented_items' , views.ShowMyPaymentedItems , basename = 'suppliar_check_order')

urlpatterns = [
    path('signup' , views.UserSignupApiView.as_view()),
    path('login/', obtain_jwt_token),
    path('verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify'),
    path('edit_profile/' , include(router.urls)),
    path('api-token-refresh/', refresh_jwt_token),
]
