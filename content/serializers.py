from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer , SerializerMethodField

from .models import (Refrigerator , Television , Laptob , 
                    Mobile , Book , Stationery , TopProduct , 
                    AmazingOffer , BaseItem)

class RefrigeratorListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Refrigerator
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class RefrigeratorDetailSerilizer(ModelSerializer):
    class Meta:
        model = Refrigerator
        fields = '__all__'

class TelevisionListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Television
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class TelevisionDetailSerilizer(ModelSerializer):
    class Meta:
        model = Television
        fields = '__all__'

class LaptobListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Laptob
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class LaptobDetailSerilizer(ModelSerializer):
    class Meta:
        model = Laptob
        fields = '__all__'

class MobileListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Mobile
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class MobileDetailSerilizer(ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

class BookListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class BookDetailSerilizer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StationeryListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Stationery
        fields = ('name' , 'brand' , 'category' , 'price' , 'detail')

class StationeryDetailSerilizer(ModelSerializer):
    class Meta:
        model = Stationery
        fields = '__all__'

class TopProductSerializer(ModelSerializer):
    product = SerializerMethodField()
    price = SerializerMethodField()
    # image = SerializerMethodField()

    def get_product(self , topproduct):
        return topproduct.product.name

    def get_price(self , topproduct):
        return topproduct.product.price

    # def get_image(self , topproduct):
    #     return topproduct.product.image    

    class Meta:
        model = TopProduct
        fields = ('product' , 'price' , 'product_detail')

class AmazingOfferSerializer(ModelSerializer):

    product = SerializerMethodField()
    price = SerializerMethodField()

    def get_product(self , topproduct):
        return topproduct.product.name

    def get_price(self , topproduct):
        return topproduct.product.price   

    class Meta:
        model = AmazingOffer
        fields = ('product' , 'price' , 'product_detail')

class NewestItemsSerializer(ModelSerializer):
    class Meta:
        model = BaseItem
        fields = ('name' , 'category' , 'price')
