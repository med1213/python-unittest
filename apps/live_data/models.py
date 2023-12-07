from django.db import models

# Create your models here.
class LiveData(models.Model):
    title = models.CharField(max_length=255,)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title