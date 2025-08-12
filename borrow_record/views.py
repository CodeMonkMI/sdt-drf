from enum import member
from urllib import request
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from borrow_record.models import BorrowRecord
from borrow_record.serializers import BorrowBookSerializers, ReturnBookSerializers
from django.utils import timezone
from book.models import Book
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
User = get_user_model()


class BorrowBookViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = BorrowBookSerializers

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            member=self.request.user.pk, return_date__isnull=True
        )

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        find_book = Book.objects.get(pk=book.pk)
        find_book.status = Book.UNAVAILABLE
        find_book.save(update_fields=["status"])

        serializer.save(member=self.request.user)

    @swagger_auto_schema(
        operation_summary="List active borrow records",
        operation_description=(
            "Return a list of **your** currently borrowed books (i.e., records with no return date). "
            "Requires authentication. Only your own active borrow records are shown."
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Return a borrowed book",
        operation_description=(
            "Submit a request to **return** one of your borrowed books. "
            "Requires authentication. The request should identify the borrowed book/record; "
            "on success, the system records the return."
        ),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ReturnBookViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):

    serializer_class = ReturnBookSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            return_date__isnull=False, member=self.request.user
        )

    def perform_create(self, serializer):
        book: Book = serializer.validated_data["book"]
        member = self.request.user
        return_date = timezone.now()

        BorrowRecord.objects.filter(
            member=member, book=book, return_date__isnull=True
        ).update(return_date=return_date)

        book.status = Book.AVAILABLE
        book.save(update_fields=["status"])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["member"] = self.request.user.pk
        return context

    @swagger_auto_schema(
        operation_summary="List books to return",
        operation_description=(
            "Retrieve a list of books you currently have borrowed and need to return. "
            "Requires authentication. Only your own unreturned books are shown."
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Return a borrowed book",
        operation_description=(
            "Mark one of your borrowed books as returned. "
            "Requires authentication. Once processed, the book becomes available for others."
        ),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
