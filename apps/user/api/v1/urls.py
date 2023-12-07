from django.urls import path
from .register_view import RegisterView, RegisterStaffView
from .views import MyObtainTokenPairView, ListUserView, RetrieveUserView, LogoutView, ChangePasswordView, AdminChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('api/v1/login', MyObtainTokenPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/logout', LogoutView.as_view(), name='auth_logout'),
    path('api/v1/user/register', RegisterView.as_view(), name='auth_register'),
    path('api/v1/user/register_staff',
         RegisterStaffView.as_view(), name='register_staff'),
    path('api/v1/user', ListUserView.as_view(), name='user'),
    path('api/v1/user/<int:pk>', RetrieveUserView.as_view(), name='user'),
    path('api/v1/token/blacklist', TokenBlacklistView.as_view(),
         name='token_blacklist'),
    path('api/v1/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='change_password'),
     path('api/v1/admin_change_password/<int:pk>/', AdminChangePasswordView.as_view(),
         name='admin_change_password'),
    #     path('api/v1/update_profile/<int:pk>', UpdateProfileView.as_view(),
    #          name='auth_update_profile'),


]
