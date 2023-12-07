from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/district', ListCreateAPIView.as_view(), name='districts'),
    path('api/v1/district/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='district'),
]
