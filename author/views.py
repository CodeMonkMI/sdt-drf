from rest_framework.viewsets import ModelViewSet
from author.models import Author
from author.serializers import AuthorSerializers


# Create your views here.


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()
