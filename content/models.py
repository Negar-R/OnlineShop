from django.db import models

# Create your models here.

class BaseItem(models.Model):

    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100 , default = '')
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

class HomeAppliance(BaseItem):

    color = models.CharField(max_length = 60 , null = True)
    weight = models.SmallIntegerField(null = True , default = 0)


class DigitalProduct(BaseItem):
    
    color = models.CharField(max_length = 100)
    ram_Gig = models.SmallIntegerField()


class Refrigerator(HomeAppliance):
    
    voltage = models.SmallIntegerField()
    side_by_side = models.BooleanField()
    top_mount_freezer = models.BooleanField()

    def __str__(self):
        return self.name
    


class Television(HomeAppliance):

    resolution = models.CharField(max_length = 100)
    size = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Laptob(DigitalProduct):
    
    screen_size = models.CharField(max_length = 100)
    touch_screen_display = models.BooleanField()
    graphics_card = models.BooleanField()

    def __str__(self):
        return self.name


class Mobile(DigitalProduct):

    os_choices = (
        ('android' , 'Android') , 
        ('ios' , 'IOS')
    )

    sim_choices = (
        ('S' , 'Standard') , 
        ('M' , 'Micro') , 
        ('N' , 'Nano')
    )

    operation_system = models.CharField(max_length = 10 , choices = os_choices)
    display_resolution = models.CharField(max_length = 100)
    sim_card = models.CharField(max_length = 3 , choices = sim_choices)

    def __str__(self):
        return self.name


    





