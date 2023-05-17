from django.contrib import admin

from .models import profile

# Register your models here.
from .models import *

admin.site.register(emp)
admin.site.register(profile)