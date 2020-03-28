from django.db import models
from django.utils.text import slugify

# Create your models here.

class BaseItem(models.Model):

    category_choice = (('Digital_Product' , 'Digital_Product') ,
                        ('Home_Appliance' , 'Home_Appliance') ,
                        ('Educational' , 'Educational'))

    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "ItemsPic" , null = True , blank = True)
    category = models.CharField(max_length = 100 , choices = category_choice)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_date = models.DateField(null = True , blank = True)

    def __str__(self):
        return self.name
    

class HomeAppliance(BaseItem):

    color_choice = (('black' , 'black') ,
                    ('white' , 'white') ,
                    ('silver' , 'silver') ,
                    ('blue' , 'blue') ,
                    ('red' , 'red') ,
                    ('green' , 'green') ,
                    ('yellow' , 'yellow'))

    color = models.CharField(max_length = 60 , choices = color_choice , null = True)
    weight = models.SmallIntegerField(null = True , default = 0)


class DigitalProduct(BaseItem):

    color_choice = (('black' , 'black') ,
                    ('white' , 'white') ,
                    ('silver' , 'silver') ,
                    ('blue' , 'blue') ,
                    ('red' , 'red') ,
                    ('green' , 'green') ,
                    ('yellow' , 'yellow'))
    
    color = models.CharField(max_length = 100 , choices = color_choice)
    ram_Gig = models.SmallIntegerField()

class Educational(BaseItem):

    recommendede_ages = models.CharField(max_length = 200)

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

class Book(Educational):

    language_choice = (('persian' , 'persian') ,
                        ('english' , 'englih'))

    author = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    language = models.CharField(max_length = 50 , choices = language_choice)
    
    def __str__(self):
        return self.name

class Stationery(Educational):

    kind_choice = (('pen' , 'pen') ,
                    ('pencil' , 'pencil') ,
                    ('Ravan_nevis' , 'Ravan_nevis'))
    nib_choice = (('flat' , 'flat') ,
                    ('ballbearings' , 'ballbearings'))
    color_choice = (('black' , 'black') ,
                    ('white' , 'white') ,
                    ('silver' , 'silver') ,
                    ('blue' , 'blue') ,
                    ('red' , 'red') ,
                    ('green' , 'green') ,
                    ('yellow' , 'yellow'))                
    
    color = models.CharField(max_length = 100 , choices = color_choice)
    kind = models.CharField(max_length = 50 , choices = kind_choice) # medad , khodkar , ravan_nevis
    nib = models.CharField(max_length = 50 , choices = nib_choice) # anvae nok
    
    def __str__(self):
        return self.name

class TopProduct(models.Model):

    product = models.ForeignKey(BaseItem , on_delete = models.CASCADE)
    product_detail = models.URLField(max_length = 200)

    def __str__(self):
        return self.product.name

class AmazingOffer(models.Model):

    product = models.ForeignKey(BaseItem , on_delete = models.CASCADE)
    product_detail = models.URLField(max_length = 200)

    def __str__(self):
        return self.product.name