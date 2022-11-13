from django.contrib import admin

# Register your models here.
from .models import allLink,allComment


admin.site.register(allLink),
admin.site.register(allComment),