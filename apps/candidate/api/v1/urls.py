from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/candidate', ListCreateAPIView.as_view(), name='candidates'),
    path('api/v1/candidate/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='candidate'),
]
