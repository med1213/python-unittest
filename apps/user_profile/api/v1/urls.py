from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView, AdminUpdateProfileView

urlpatterns = [
    path('api/v1/user_profile', ListCreateAPIView.as_view(), name='profiles'),
    path('api/v1/user_profile/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(), name='profile'),
    path('api/v1/admin_update_profile/<int:pk>/', AdminUpdateProfileView.as_view(), name='admin-update-profile'),
]