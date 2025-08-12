from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from borrow_record.models import BorrowRecord
from borrow_record.serializers import BorrowBookSerializers, ReturnBookSerializers
from django.utils import timezone
from book.models import Book
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class BorrowBookViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = BorrowBookSerializers
    queryset = BorrowRecord.objects.filter(return_date__isnull=True)

    def perform_create(self, serializer):

        book = serializer.validated_data["book"]
        find_book = Book.objects.get(pk=book.pk)
        find_book.status = Book.UNAVAILABLE
        find_book.save(update_fields=["status"])

        serializer.save()


class ReturnBookViewSet(CreateModelMixin, GenericViewSet):
    queryset = BorrowRecord.objects.filter(return_date__isnull=False)
    serializer_class = ReturnBookSerializers

    def perform_create(self, serializer):
        book: Book = serializer.validated_data["book"]
        member = serializer.validated_data["member"]
        return_date = (
            serializer.validated_data["return_date"] or timezone.datetime.now()
        )

        BorrowRecord.objects.filter(
            member=member, book=book, return_date__isnull=True
        ).update(return_date=return_date)

        book.status = Book.AVAILABLE
        book.save(update_fields=["status"])
