from django.contrib import admin

# Register your models here.
from basic_app.models import Student, School

admin.site.register(School)
admin.site.register(Student)