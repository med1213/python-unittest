from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/period', ListCreateAPIView.as_view(), name='periods'),
    path('api/v1/period/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='period'),
]
