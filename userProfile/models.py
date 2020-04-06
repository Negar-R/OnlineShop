from django.db import models
from django.contrib.auth.models import User

import uuid

class UserInformation(models.Model):

    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.address
    
class UserProfile(models.Model):

    user = models.OneToOneField(User , related_name = 'users' , on_delete = models.CASCADE)
    phone = models.CharField(max_length = 11)
    address = models.ManyToManyField(UserInformation , related_name = 'informations' , related_query_name = 'information')
    is_verified = models.BooleanField(default = False) # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default = uuid.uuid4)

    def __str__(self):
        return self.user.username
       