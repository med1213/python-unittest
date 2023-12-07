
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VillageGetSerializer, VillagePostSerializer
from apps.village.models import Village
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY, 
                            description="depth", 
                            type=openapi.TYPE_BOOLEAN)

DISTRICT = "district"
district = openapi.Parameter(DISTRICT, openapi.IN_QUERY,
                           description="district",
                           type=openapi.TYPE_STRING)

VILLAGE = "village"
village = openapi.Parameter(VILLAGE, openapi.IN_QUERY,
                           description="village",
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
    queryset = Village.objects.all()
    serializer_class = VillagePostSerializer

    @swagger_auto_schema(manual_parameters=[depth, district, village, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Village.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_district(queryset)
        queryset = self.get_village(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = VillageGetSerializer if depth else VillagePostSerializer
        return queryset
    
    def get_district(self, queryset):
        district = self.request.query_params.get(DISTRICT)
        if not district:
            return queryset
        if district is not None:
            queryset = queryset.filter(
                district_id=district)
        return queryset

    def get_village(self, queryset):
        village = self.request.query_params.get(VILLAGE)
        if not village:
            return queryset
        if village is not None:
            queryset = queryset.filter(
                village=village)
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
    queryset = Village.objects.all()
    serializer_class = VillagePostSerializer
