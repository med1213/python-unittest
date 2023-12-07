from django.db import models
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete
from apps.period.models import Period

# Create your models here.
class Post(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = ImageField(verbose_name='Image', upload_to="", blank=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("post")
    verbose_name_plural = ("posts")

def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
