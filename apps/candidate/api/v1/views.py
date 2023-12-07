
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.candidate.models import Candidate
from .serializers import CandidateGetSerializer, CandidatePostSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

boolean_mapping = {
    "true": True,
    "false": False
}

ACTIVE = "is_active"
is_active = openapi.Parameter(ACTIVE, openapi.IN_QUERY,
                            description="active",
                            type=openapi.TYPE_BOOLEAN)

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY,
                          description="depth",
                          type=openapi.TYPE_BOOLEAN)

PHONE_NUMBER = "phone_number"
phone_number = openapi.Parameter(PHONE_NUMBER, openapi.IN_QUERY,
                                 description="phone_number",
                                 type=openapi.TYPE_STRING)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidatePostSerializer

    @swagger_auto_schema(manual_parameters=[depth, phone_number, is_active])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Candidate.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_phone_number(queryset)
        queryset = self.get_active(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        if (depth):
            self.serializer_class = CandidateGetSerializer
        else:
            self.serializer_class = CandidatePostSerializer
        return queryset

    def get_phone_number(self, queryset):
        phone_number = self.request.query_params.get(PHONE_NUMBER)
        if not phone_number:
            return queryset
        if phone_number is not None:
            queryset = queryset.filter(
                phone_number=phone_number)
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
    queryset = Candidate.objects.all()
    serializer_class = CandidatePostSerializer
