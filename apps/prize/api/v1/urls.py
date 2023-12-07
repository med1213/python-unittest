from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/prize', ListCreateAPIView.as_view(), name='prizes'),
    path('api/v1/prize/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='prize'),
]
