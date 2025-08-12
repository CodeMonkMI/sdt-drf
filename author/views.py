from rest_framework.viewsets import ModelViewSet
from author.models import Author
from author.serializers import AuthorSerializers
from api.permissions import IsLibrarian
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()

    permission_classes = [IsAuthenticated, IsLibrarian]
