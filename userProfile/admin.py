from django.contrib import admin

from .models import UserProfile , UserInformation

admin.site.register(UserProfile)
admin.site.register(UserInformation)

