from django.db import models
class Student(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=64)
    mobile=models.IntegerField()
    city=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

# Create your models here.
