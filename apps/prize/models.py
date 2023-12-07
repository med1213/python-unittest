from django.db import models
from apps.prize_type.models import PrizeType
from django.urls import reverse


class Prize(models.Model):

    prize_type = models.ForeignKey(
        PrizeType,  on_delete=models.CASCADE, related_name='prize')
    prize = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Prize")
    verbose_name_plural = ("Prizes")
