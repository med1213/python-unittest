from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/post', ListCreateAPIView.as_view(), name='posts'),
    path('api/v1/post/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='post'),
]