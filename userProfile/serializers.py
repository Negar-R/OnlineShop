from rest_framework import serializers
from rest_framework.response import Response

from django.contrib.auth.models import User

from userProfile import models

class SignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 11)
    password1 = serializers.CharField(label='password' , min_length = 4 , max_length = 100 , style = {'input_type' : 'password'})
    password2 = serializers.CharField(label='password confirm' , min_length = 4 , max_length = 100 , style = {'input_type' : 'password'})

    def get_clean_password(self):
        password1 = self.data.get("password1")
        password2 = self.data.get("password2")
        print(password1, password2)
        if not password1 or not password2 or password1 != password2:
            raise serializers.ValidationError(_('passwords must match'))
        return password2

    def create(self, validated_data):
        clean_password = self.get_clean_password()
        if clean_password:
            user, _ = User.objects.get_or_create(username = validated_data['username'] , email = validated_data['email'])
            user.set_password(clean_password)
            user.save()
            profile, _ = models.UserProfile.objects.get_or_create(user = user , phone = validated_data['phone'])
            return user

    class Meta:
        model = User
        fields = ('username' , 'email' , 'phone' , 'password1', 'password2')
        write_only_fields = ('password1', 'password2') #to make sure passwords are not displayed



class UpdateProfileSerializer(serializers.Serializer):
    
    address = serializers.CharField(max_length = 200)