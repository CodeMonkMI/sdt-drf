from rest_framework import serializers
from borrow_record.models import BorrowRecord
from book.models import Book
from borrow_record.models import BorrowRecord
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
        ]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
        ]


class BorrowBookSerializers(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField(
        method_name="get_member_name",
        read_only=True,
    )
    book_title = serializers.SerializerMethodField(
        method_name="get_book_name",
        read_only=True,
    )

    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(status=Book.AVAILABLE)
    )

    class Meta:
        model = BorrowRecord
        fields = [
            "member",
            "book",
            "borrow_date",
            "due_date",
            "member_name",
            "book_title",
        ]

        extra_kwargs = {
            "member": {"write_only": True},
            "book": {"write_only": True},
        }

    def get_member_name(self, borrow: BorrowRecord):
        return f"{borrow.member.first_name} {borrow.member.last_name}"

    def get_book_name(self, borrow: BorrowRecord):
        return borrow.book.title

    def validate_book(self, book):
        if book.status == Book.UNAVAILABLE:
            raise serializers.ValidationError("You requested book is unavailable!")
        return book


class ReturnBookSerializers(serializers.ModelSerializer):

    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(status=Book.UNAVAILABLE)
    )

    class Meta:
        model = BorrowRecord
        fields = [
            "member",
            "book",
            "created_at",
            "return_date",
        ]
        extra_kwargs = {
            "member": {"write_only": True},
            "book": {"write_only": True},
            "created_at": {"read_only": True},
        }

    def validate_book(self, book):
        if book.status == Book.AVAILABLE:
            raise serializers.ValidationError("You requested book is not available!")
        return book

    def validate(self, attrs):
        member = attrs["member"]
        book = attrs["book"]
        find_records = BorrowRecord.objects.filter(
            member=member,
            book=book,
            return_date__isnull=True,
        ).exists()
        if not find_records:
            raise serializers.ValidationError("No records with given information!")
        return attrs
