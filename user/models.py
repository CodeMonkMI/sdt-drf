from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    ACTIVE = "active"
    INACTIVE = "inactive"
    STATUS_CHOICES = [
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    membership_date = models.DateTimeField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
