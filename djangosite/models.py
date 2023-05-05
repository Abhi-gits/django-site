from django.db import models

# Create your models here.


class emp(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=150)
    joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name