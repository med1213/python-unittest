from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete

# Create your models here.
class UserProfile(models.Model):

    class Gender(models.TextChoices):
        Male = "Male"
        Female = "Female"

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner_user_profile",)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=Gender.choices)
    profile_pic = ImageField(verbose_name='Image', upload_to="", blank=True)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']
        verbose_name = ("user_profile")
        verbose_name_plural = ("user_profiles")

def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)