from django.contrib import admin
from .models import Student
# Register your models here.

model_lists = [Student]

admin.site.register(model_lists)

