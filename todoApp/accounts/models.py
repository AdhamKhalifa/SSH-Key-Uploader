
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    
    # First name
    f_name = models.CharField(blank=True, max_length=20, verbose_name='first name', null=True)

    # Last Name
    l_name = models.CharField(blank=True, max_length=20, verbose_name='last name', null=True)
   
    # Username
    u_name = models.CharField(blank=True, max_length=30, unique=True, verbose_name='user name', null=True)

    # Email
    e_mail = models.EmailField(max_length=254, unique=True, verbose_name='email address', null=True)