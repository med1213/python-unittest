from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/village', ListCreateAPIView.as_view(), name='villages'),
    path('api/v1/village/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='village'),
]
