from django.urls import path , include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from userProfile import views

urlpatterns = [
    path('signup' , views.UserSignupApiView.as_view()),
    path('login', obtain_jwt_token),
    path('update_profile' , views.UpdateProfileView.as_view()),
    path('api-token-refresh/', refresh_jwt_token),
]
