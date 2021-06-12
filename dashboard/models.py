from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="df.jpg",null=True, blank=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.name)






# def create_profile(sender,instance,created,**kwargs):
# if created:
