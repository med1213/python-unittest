from django.db import models
from apps.prize_type.models import PrizeType
from apps.period_type.models import PeriodType
import datetime
from django.utils.timezone import now, localtime


class Period(models.Model):
    period = models.CharField(max_length=255)
    prize_type = models.ManyToManyField(
        PrizeType, related_name='prize_period')
    period_type = models.ManyToManyField(
        PeriodType, related_name='prize_period_id')
    open_date = models.DateTimeField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    related_periods = models.ManyToManyField(
        'self', symmetrical=False, related_name='related_to_periods', blank=True)

    def __str__(self):
        return self.period

    @property
    def active(self):
        return self.close_date > localtime(now())

    def save(self, *args, **kwargs):
        self.open_date = localtime(now())
        self.close_date = self.open_date + datetime.timedelta(minutes=1)
        return super(Period, self).save(*args, **kwargs)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Period")
    verbose_name_plural = ("Periods")
