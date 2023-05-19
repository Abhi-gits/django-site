from django.db import models
from django.contrib.auth.models import User
from .helpers import *

# Create your models here.


class profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_verified = models.BooleanField(default = False)
    token = models. CharField(max_length=100)


class emp(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    phone = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=150)
    joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(emp, self).save(*args, **kwargs)
        
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.name
    