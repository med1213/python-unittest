from django.db import models
from apps.prize.models import Prize
from apps.bill.models import Bill


class Winner(models.Model):
    prize = models.ForeignKey(
        Prize,  on_delete=models.CASCADE, related_name='winner')
    lottery_bill = models.ForeignKey(
        Bill,  on_delete=models.CASCADE, related_name='winner')
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Winner")
    verbose_name_plural = ("Winners")
