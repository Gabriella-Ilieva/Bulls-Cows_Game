from django.contrib.auth import models as auth_model
from django.db import models


class PlayerAccount(auth_model.AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result

