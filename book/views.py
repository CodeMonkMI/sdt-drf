from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import BookSerializers, BookCreteSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.permissions import IsLibrarianOrReadOnly, IsLibrarian

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
