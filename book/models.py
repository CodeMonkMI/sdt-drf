from pyexpat import model
from uuid import uuid4
from django.db import models
from author.models import Author

# Create your models here.


class Book(models.Model):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    STATUS_CHOICES = [
        (AVAILABLE, "available"),
        (UNAVAILABLE, "unavailable"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
