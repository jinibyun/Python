from django.db import models

# Create your models here.
from django.urls import reverse


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # the below is about enabling passing parameter
    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
