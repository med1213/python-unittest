from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/winner', ListCreateAPIView.as_view(), name='winners'),
    path('api/v1/winner/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='winner'),
]
