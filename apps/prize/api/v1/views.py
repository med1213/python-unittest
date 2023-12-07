from drf_yasg import openapi
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PrizeGetSerializer, PrizePostSerializer
from apps.prize.models import Prize


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY,
                          description="depth",
                          type=openapi.TYPE_BOOLEAN)

boolean_mapping = {
    "true": True,
    "false": False
}
ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                            description="active",
                            type=openapi.TYPE_BOOLEAN)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizePostSerializer

    @swagger_auto_schema(manual_parameters=[depth, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Prize.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        if (depth):
            self.serializer_class = PrizeGetSerializer
        else:
            self.serializer_class = PrizePostSerializer
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
    queryset = Prize.objects.all()
    serializer_class = PrizePostSerializer
