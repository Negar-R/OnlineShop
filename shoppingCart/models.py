from django.db import models
from django.contrib.auth.models import User

import content
import userProfile

# Create your models here.

class Shopping_Cart(models.Model):

    category_choices = (
        ('Home Applience' , 'Home Applience') , 
        ('Digital Product' , 'Digital Product')
    )

    status_choices = (
        ('on_cart' , 'on_cart') ,
        ('payed' , 'payed')
    )

    user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    item = models.ForeignKey(content.models.BaseItem , on_delete = models.CASCADE , null = True)
    quantity = models.IntegerField()
    status = models.CharField(max_length = 10 , choices = status_choices , null = True)   

    def __str__(self):
        return self.item.name
    