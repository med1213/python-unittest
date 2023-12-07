
import random
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LotteryGetBillSerializer, LotteryPostBillSerializer
from apps.winner.api.v1.serializers import WinnerSerializer
from apps.bill.models import Bill
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from apps.winner.models import Winner
from apps.prize.models import Prize
from rest_framework.views import APIView


PRIZE = "prize"
prize = openapi.Parameter(PRIZE, openapi.IN_QUERY,
                          description="Prize ID to filter by",
                          type=openapi.TYPE_INTEGER)
PERIOD = "period"
period = openapi.Parameter(PERIOD, openapi.IN_QUERY,
                           description="Comma-separated list of periods to filter by id",
                           type=openapi.TYPE_STRING)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = LotteryPostBillSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = LotteryPostBillSerializer


class RandomLuckyBillAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[prize, period])
    def get(self, request, *args, **kwargs):
        period = request.query_params.get(PERIOD, '').strip()
        period_ids = [int(p) for p in period.split(',') if p.isdigit()]
        queryset = Bill.objects.filter(
            is_draw=False, is_active=True, period__in=period_ids)
        random_lucky_bill = self.random_lucky_bill(queryset)
        if not random_lucky_bill:
            return Response({'detail': 'No lucky bill available for the specified period.'})
        serializer = LotteryGetBillSerializer(random_lucky_bill)
        return Response(serializer.data)

    def random_lucky_bill(self, queryset):
        prize_id = self.request.query_params.get(PRIZE)
        if not prize_id:
            return None
        prize_instance = Prize.objects.filter(id=prize_id).first()
        if not prize_instance:
            return None
        lucky_bills = list(queryset)
        if not lucky_bills:
            return None
        random_lucky_bill = random.choice(lucky_bills)
        Winner.objects.create(
            prize=prize_instance, lottery_bill=random_lucky_bill, is_active=True)
        random_lucky_bill.is_draw = True
        random_lucky_bill.save()
        return random_lucky_bill


# class RandomLuckyBillAPIView(APIView):
#     @swagger_auto_schema(manual_parameters=[prize, period])
#     def get(self, request, *args, **kwargs):
#         period = request.query_params.get(PERIOD, '').strip()
#         period_ids = [int(p) for p in period.split(',') if p.isdigit()]
#         queryset = Bill.objects.filter(
#             is_draw=False, is_active=True, period__in=period_ids)
#         random_lucky_bill = self.random_lucky_bill(queryset)
#         if not random_lucky_bill:
#             return Response({'detail': 'No lucky bill available for the specified period.'})
#         serializer = LotteryGetBillSerializer(random_lucky_bill)
#         return Response(serializer.data)

#     def random_lucky_bill(self, queryset):
#         lucky_bills = list(queryset)
#         if not lucky_bills:
#             return None
#         random_lucky_bill = random.choice(lucky_bills)
#         return random_lucky_bill

#     @swagger_auto_schema(request_body=WinnerSerializer)
#     def post(self, request, *args, **kwargs):
#         serializer = WinnerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         prize_instance = serializer.validated_data['prize']
#         lottery_bill = serializer.validated_data['lottery_bill']
#         try:
#             winner = Winner.objects.get(prize=prize_instance, is_active=True)
#             return Response({'detail': f'The prize "{prize_instance.name}" has already been claimed.'})
#         except Winner.DoesNotExist:
#             pass
#         winner = Winner.objects.create(
#             prize=prize_instance, lottery_bill=lottery_bill, is_active=True)
#         lottery_bill.is_draw = True
#         lottery_bill.save()
#         return Response({'detail': f'Congratulations! You have won the prize "{prize_instance.name}".'})
