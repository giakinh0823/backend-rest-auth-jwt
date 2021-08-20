from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, null=False)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username