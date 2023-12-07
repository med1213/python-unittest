from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/about', ListCreateAPIView.as_view(), name='abouts'),
    path('api/v1/about/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='about'),
]
