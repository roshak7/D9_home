from rest_framework import serializers
from app.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source="author.id")
    author_name = serializers.CharField(read_only=True, source="author.name")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "author": {
                "id": instance.author.id,
                "name": instance.author.name,
            }
        }

    def to_internal_value(self, data):
        return {
            "title": data.get("title"),
            "author_id": data.get("author_id"),
        }

    def create(self, validated_data):
        author_id = validated_data.pop("author_id", None)

        if not author_id:
            raise Exception("incorrect author id")

        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExit:
            raise Exception("Author Does Not Exit")

        return Book.objects.create(author=author, **validated_data)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_id', 'author_name']


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class AuthorDetailedSerializer(serializers.ModelSerializer):
    books = BookAuthorSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']