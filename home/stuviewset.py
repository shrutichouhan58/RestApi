from rest_framework import serializers
from .models import Student
from rest_framework import viewsets
from home.stuserializer import StuSerializer
class StuViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StuSerializer