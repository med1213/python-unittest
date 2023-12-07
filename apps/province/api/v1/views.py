
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProvinceSerializer
from apps.province.models import Province

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

boolean_mapping = {
    "true": True,
    "false": False
}

PROVINCE = "province"
province = openapi.Parameter(PROVINCE, openapi.IN_QUERY,
                           description="province",
                           type=openapi.TYPE_STRING)

ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                            description="active",
                            type=openapi.TYPE_BOOLEAN)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


    @swagger_auto_schema(manual_parameters=[province, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Province.objects.all()
        queryset = self.get_province(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_province(self, queryset):
        province = self.request.query_params.get(PROVINCE)
        if not province:
            return queryset
        if province is not None:
            queryset = queryset.filter(
                province=province)
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
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
