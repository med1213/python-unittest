
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.winner.models import Winner
from .serializers import WinnerSerializer, WinnerPostSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

boolean_mapping = {
    "true": True,
    "false": False
}
RELATED_ID = "related_id"
related_id = openapi.Parameter(RELATED_ID, openapi.IN_QUERY,
                               description="related_id",
                               type=openapi.TYPE_BOOLEAN)
PERIOD = "period"
period = openapi.Parameter(PERIOD, openapi.IN_QUERY,
                           description="period",
                           type=openapi.TYPE_INTEGER)

PRIZE = "prize"
prize = openapi.Parameter(PRIZE, openapi.IN_QUERY,
                          description="prize",
                          type=openapi.TYPE_INTEGER)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerPostSerializer

    @swagger_auto_schema(manual_parameters=[related_id, period, prize])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Winner.objects.all()
        queryset = self.filter_related_id(queryset)
        queryset = self.filter_period(queryset)
        queryset = self.filter_prize(queryset)

        return queryset

    def filter_related_id(self, queryset):
        raw_depth = self.request.query_params.get(RELATED_ID)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = WinnerSerializer if depth else WinnerPostSerializer
        return queryset

    def filter_period(self, queryset):
        period = self.request.query_params.get(PERIOD)
        if not period:
            return queryset
        if period is not None:
            queryset = queryset.filter(
                lottery_bill__period__id=period)
        return queryset

    def filter_prize(self, queryset):
        prize = self.request.query_params.get(PRIZE)
        if not prize:
            return queryset
        if prize is not None:
            queryset = queryset.filter(
                prize__id=prize)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
