from django.db import models

from django.contrib.auth.models import User , BaseUserManager , PermissionsMixin , AbstractBaseUser


class UserProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone = models.CharField(max_length = 11)
    address = models.TextField() 

    def __str__(self):
        return self.user.username
       
     