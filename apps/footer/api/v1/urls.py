from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/footer/', ListCreateAPIView.as_view(), name='footer_list'),
    path('api/v1/footer/<int:pk>/',
         RetrieveUpdateDestroyAPIView.as_view(), name='footer_detail'),
]
