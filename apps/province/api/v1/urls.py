from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/province', ListCreateAPIView.as_view(), name='province_list'),
    path('api/v1/province/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='provinces'),
]
