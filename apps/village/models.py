from django.db import models
from apps.province.models import Province
from apps.district.models import District

# Create your models here.


class Village(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="village")
    village = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("village")
    verbose_name_plural = ("villages")

