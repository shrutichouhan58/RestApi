
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.models import Student
from home.stuserializer import StuSerializer
from home.stuviewset import StuViewset

router=routers.DefaultRouter()
router.register(r'students',StuViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
