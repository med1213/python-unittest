from django.db import models


class Footer(models.Model):
    address = models.TextField()
    email = models.EmailField(max_length=100)
    instagram_url = models.URLField(max_length=100)
    facebook_url = models.URLField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("footer")
    verbose_name_plural = ("footers")