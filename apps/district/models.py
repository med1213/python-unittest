from django.db import models
from apps.province.models import Province

# Create your models here.


class District(models.Model):
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name='district')
    district = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("district")
    verbose_name_plural = ("district")
