from rest_framework import serializers
from book.models import Book
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
        ]


class BookSerializers(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "isbn",
            "category",
            "status",
            "author",
        ]


class BookCreteSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "category",
            "status",
            "author",
        ]
