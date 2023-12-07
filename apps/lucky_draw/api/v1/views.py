from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LuckyDrawSerializer
from apps.lucky_draw.models import LuckyDraw
import random
from django.http import JsonResponse
from rest_framework.views import APIView
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


class LuckyDrawListCreateAPIView(ListCreateAPIView):
    queryset = LuckyDraw.objects.all()
    serializer_class = LuckyDrawSerializer

    @swagger_auto_schema(manual_parameters=[is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = LuckyDraw.objects.all()
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


class LuckyDrawRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LuckyDraw.objects.all()
    serializer_class = LuckyDrawSerializer


class LuckyDrawAPI(APIView):
    queryset = LuckyDraw.objects.all()
    serializer_class = LuckyDrawSerializer

    @swagger_auto_schema(manual_parameters=[is_active])
    def get(self, request, *args, **kwargs):
        return self.random_item_name(request)

    def random_item_name(self, request):
        lucky_draws = LuckyDraw.objects.filter(is_active=True)
        if not lucky_draws:
            return JsonResponse({"error": "No active lucky draws found."}, status=404)
        random_lucky_draw = random.choice(lucky_draws)
        return JsonResponse({"item_name": random_lucky_draw.item_name})
