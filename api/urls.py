from django.urls import path, include


from .views import upload
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/images/1/', upload)
]