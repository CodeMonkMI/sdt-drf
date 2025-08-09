from pyexpat import model
from uuid import uuid4
from django.db import models

from member.models import Member
from book.models import Book

# Create your models here.


class BorrowRecord(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="borrowed"
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.book.title} borrowed by {self.member.name}"
