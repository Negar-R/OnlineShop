from django.urls import path , include

from userProfile import views

urlpatterns = [
    path('signup' , views.UserSignupApiView.as_view()),
    path('login' , views.UserLoginApiView.as_view()),
    path('update_profile' , views.UpdateProfileView.as_view()),
]
