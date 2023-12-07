
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DistrictGetSerializer, DistrictPostSerializer
from apps.district.models import District
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY, 
                            description="depth", 
                            type=openapi.TYPE_BOOLEAN)

PROVINCE = "province"
province = openapi.Parameter(PROVINCE, openapi.IN_QUERY,
                           description="province",
                           type=openapi.TYPE_STRING)

DISTRICT = "district"
district = openapi.Parameter(DISTRICT, openapi.IN_QUERY,
                           description="district",
                           type=openapi.TYPE_STRING)

boolean_mapping = {
    "true": True,
    "false": False
}

ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                            description="active",
                            type=openapi.TYPE_BOOLEAN)


class ListCreateAPIView(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictPostSerializer

    @swagger_auto_schema(manual_parameters=[depth, province, district, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = District.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_province(queryset)
        queryset = self.get_district(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = DistrictGetSerializer if depth else DistrictPostSerializer
        return queryset
    
    def get_province(self, queryset):
        province = self.request.query_params.get(PROVINCE)
        if not province:
            return queryset
        if province is not None:
            queryset = queryset.filter(
                province_id=province)
        return queryset

    def get_district(self, queryset):
        district = self.request.query_params.get(DISTRICT)
        if not district:
            return queryset
        if district is not None:
            queryset = queryset.filter(
                district=district)
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
    queryset = District.objects.all()
    serializer_class = DistrictPostSerializer
