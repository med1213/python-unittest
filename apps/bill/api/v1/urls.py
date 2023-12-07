from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RandomLuckyBillAPIView

urlpatterns = [
    path('api/v1/bill', ListCreateAPIView.as_view(), name='bills'),
    path('api/v1/bill/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='bill'),
    path('api/v1/random',
         RandomLuckyBillAPIView.as_view(), name='random'),
]
