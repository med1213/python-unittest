from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/slide', ListCreateAPIView.as_view(), name='slides'),
    path('api/v1/slide/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='slide'),
]
