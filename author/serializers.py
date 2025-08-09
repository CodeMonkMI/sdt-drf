from rest_framework import serializers
from author.models import Author


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "biography"]
