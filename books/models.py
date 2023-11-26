from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
#from helpers.models import TrackingModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import jwt
from datetime import datetime, timedelta


from django.conf import settings

from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    file = models.ImageField(upload_to='images/')
    
    

    def __str__(self):
        return self.name + '  ->  ' + self.description
    

class book_user(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        real_name=models.CharField(max_length=40)



    