from django.db import models
from apps.period.models import Period
from apps.candidate.models import Candidate
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class Bill(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='lottery_bill')
    period = models.ForeignKey(
        Period, on_delete=models.CASCADE, related_name='lottery_bill', blank=True, null=True)
    bill_number = models.CharField(max_length=30)
    total_cost = models.IntegerField()
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    is_draw = models.BooleanField(default=False)
    device_number = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Lottery_bill")
    verbose_name_plural = ("Lottery_bill")


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
