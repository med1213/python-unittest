from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/period_type', ListCreateAPIView.as_view(), name='period_types'),
    path('api/v1/period_type/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='period_type'),
]
