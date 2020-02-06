from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer

from .models import Refrigerator , Television , Laptob , Mobile

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