from django.urls import path
from .views import LuckyDrawListCreateAPIView, LuckyDrawRetrieveUpdateDestroyAPIView, LuckyDrawAPI

urlpatterns = [
    path('api/v1/lucky_draw', LuckyDrawListCreateAPIView.as_view(), name='lucky_draws'),
    path('api/v1/lucky_draw/<int:pk>/',
         LuckyDrawRetrieveUpdateDestroyAPIView.as_view(), name='lucky_draw'),
    path('api/v1/luck_draw_random',
         LuckyDrawAPI.as_view(), name='lucky_draw_random'),
]
