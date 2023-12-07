from django.db import models


class LuckyDraw(models.Model):
    item_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lucky Draw"
        verbose_name_plural = "Lucky Draws"
