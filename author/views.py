from rest_framework.viewsets import ModelViewSet
from author.models import Author
from author.serializers import AuthorSerializers
from api.permissions import IsLibrarian
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()
    http_method_names = ["get", "post", "patch", "destroy", "options", "head", "delete"]
    permission_classes = [IsAuthenticated, IsLibrarian]

    @swagger_auto_schema(
        operation_summary="List authors",
        operation_description=(
            "Returns a list of all authors. " "Accessible only by librarians or admins."
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create author",
        operation_description=(
            "Create a new author with the provided information. "
            "Accessible only by librarians or admins."
        ),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve author",
        operation_description=(
            "Fetch details of a single author by ID. "
            "Accessible only by librarians or admins."
        ),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update author (partial)",
        operation_description=(
            "Partially update the details of an author by ID. "
            "Accessible only by librarians or admins."
        ),
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete author",
        operation_description=(
            "Delete an author by ID. " "Accessible only by librarians or admins."
        ),
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
