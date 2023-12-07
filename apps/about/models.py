from django.db import models
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = ImageField(verbose_name='Image', upload_to="", blank=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ("about")
        verbose_name_plural = ("abouts")


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
