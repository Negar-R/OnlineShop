from django.db import models

import userProfile
import shoppingCart

# Create your models here.

class Suppliar_Check_Order(models.Model):

    status_choices = (
        ('ready' , 'Ready to send') , 
        ('on_process' , 'On Process') ,
    )

    reciever = models.ForeignKey(userProfile.models.UserProfile , on_delete = models.CASCADE)
    factor = models.ForeignKey(shoppingCart.models.Shopping_Cart , on_delete = models.CASCADE , null = True , blank = True)
    status = models.CharField(max_length = 50 , choices = status_choices)
