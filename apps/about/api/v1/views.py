from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AboutSerializer
from apps.about.models import About

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                            description="active",
                            type=openapi.TYPE_BOOLEAN)

boolean_mapping = {
    "true": True,
    "false": False
}


class ListCreateAPIView(ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    @swagger_auto_schema(manual_parameters=[is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = About.objects.all()
        queryset = self.get_active(queryset)
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
    queryset = About.objects.all()
    serializer_class = AboutSerializer
