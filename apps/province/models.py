from django.db import models

# Create your models here.


class Province(models.Model):
    province = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Province")
    verbose_name_plural = ("Provinces")
