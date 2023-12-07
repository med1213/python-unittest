from django.db import models


class PeriodType(models.Model):

    period_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("PeriodType")
    verbose_name_plural = ("PeriodTypes")
