from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/prize_type', ListCreateAPIView.as_view(), name='prize_types'),
    path('api/v1/prize_type/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='prize_type'),
]
