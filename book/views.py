from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import BookSerializers, BookCreteSerializers

# Create your views here.


class BookViewSet(ModelViewSet):
    # serializer_class = BookSerializers
    queryset = Book.objects.all()
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ["POST", "PATCH"]:
            return BookCreteSerializers
        return BookSerializers
