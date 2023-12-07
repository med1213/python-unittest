from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from apps.user_profile.models import UserProfile
from .serializers import UserProfileGetSerializer, UserProfilePostSerializer, UpdateUserprofileAdminSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import  IsAdminUser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY,
                          description="depth",
                          type=openapi.TYPE_BOOLEAN)

USER = "user"
user = openapi.Parameter(USER, openapi.IN_QUERY,
                         description="user",
                         type=openapi.TYPE_STRING)

ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                              description="active",
                              type=openapi.TYPE_BOOLEAN)

boolean_mapping = {
    "true": True,
    "false": False
}

# Create your views here.


class ListCreateAPIView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserProfilePostSerializer

    @swagger_auto_schema(manual_parameters=[depth, user, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_user(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = UserProfileGetSerializer if depth else UserProfilePostSerializer
        return queryset

    def get_user(self, queryset):
        user = self.request.query_params.get(USER)
        if not user:
            return queryset
        if user is not None:
            queryset = queryset.filter(
                owner__id=user)
        return queryset

    def get_active(self, queryset):
        is_active = self.request.query_params.get(ACTIVE)
        if not is_active:
            return queryset
        is_active = boolean_mapping[is_active]
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = UserProfilePostSerializer


class AdminUpdateProfileView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UpdateUserprofileAdminSerializer

