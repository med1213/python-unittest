from django.db import models
from apps.province.models import Province
from apps.district.models import District
from apps.village.models import Village


class Candidate(models.Model):
    province = models.ForeignKey(
        Province,  on_delete=models.CASCADE, related_name='candidate',)
    district = models.ForeignKey(
        District,  on_delete=models.CASCADE, related_name='candidate',)
    village = models.ForeignKey(
        Village,  on_delete=models.CASCADE, related_name='candidate',)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Candidate")
    verbose_name_plural = ("Candidates")
