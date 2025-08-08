from pyexpat import model
from uuid import uuid4
from django.db import models
from author.models import Author

# Create your models here.


class Member(models.Model):
    ACTIVE = "active"
    INACTIVE = "inactive"
    STATUS_CHOICES = [
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    membership_date = models.DateTimeField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
