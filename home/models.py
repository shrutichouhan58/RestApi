from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    mobile=models.IntegerField()
    def __str__(self) -> str:
        return self.name