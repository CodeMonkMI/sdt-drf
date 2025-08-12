from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import BookSerializers, BookCreteSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.permissions import IsLibrarianOrReadOnly, IsLibrarian
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class BookViewSet(ModelViewSet):

    # serializer_class = BookSerializers
    queryset = Book.objects.all()
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]
    # permission_classes = [IsLibrarianOrReadOnly] # custom permission class

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ["POST", "PATCH"]:
            return BookCreteSerializers
        return BookSerializers

    def get_permissions(self):
        if self.action in ["create", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsLibrarian()]
        return super().get_permissions()

    @swagger_auto_schema(
        operation_summary="List books",
        operation_description=(
            "Return a list of books. "
            "Accessible to authenticated members, librarians, and admins."
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create book",
        operation_description=(
            "Create a new book with the provided information. "
            "Accessible only by librarians or admins."
        ),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve book",
        operation_description=(
            "Fetch details of a single book by ID. "
            "Accessible only by librarians or admins."
        ),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update book (partial)",
        operation_description=(
            "Partially update the details of a book by ID. "
            "Accessible only by librarians or admins."
        ),
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete book",
        operation_description=(
            "Delete a book by ID. " "Accessible only by librarians or admins."
        ),
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
