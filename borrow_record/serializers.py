from enum import member
from rest_framework import serializers
import borrow_record
from borrow_record.models import BorrowRecord
from book.models import Book
from borrow_record.models import BorrowRecord
from django.contrib.auth import get_user_model

User = get_user_model()


class BorrowBookSerializers(serializers.ModelSerializer):

    book_title = serializers.CharField(
        source="book.title",
        read_only=True,
    )

    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(status=Book.AVAILABLE)
    )

    class Meta:
        model = BorrowRecord
        fields = [
            "book",
            "borrow_date",
            "due_date",
            "book_title",
        ]

        extra_kwargs = {
            "book": {"write_only": True},
        }

    def validate_book(self, book):
        if book.status == Book.UNAVAILABLE:
            raise serializers.ValidationError("You requested book is unavailable!")
        return book


class ReturnBookSerializers(serializers.ModelSerializer):

    book = serializers.PrimaryKeyRelatedField(queryset=[], write_only=True)
    book_title = serializers.CharField(
        source="book.title",
        read_only=True,
    )
    returned_at = serializers.DateTimeField(
        source="return_date",
        read_only=True,
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if "member" in self.context:

            member = self.context["member"]
            # data = BorrowRecord.objects.filter(member=member, return_date__isnull=True)
            self.fields["book"].queryset = Book.objects.filter(
                borrows__member=member, borrows__return_date__isnull=True
            ).distinct()

    class Meta:
        model = BorrowRecord
        fields = [
            "book_title",
            "book",
            "returned_at",
        ]

    def validate_book(self, book):
        if book.status == Book.AVAILABLE:
            raise serializers.ValidationError("You requested book is not available!")
        return book

    def validate(self, attrs):
        member = self.context["member"]
        book = attrs["book"]
        find_records = BorrowRecord.objects.filter(
            member=member,
            book=book,
            return_date__isnull=True,
        ).exists()
        if not find_records:
            raise serializers.ValidationError("No records with given information!")
        return attrs
