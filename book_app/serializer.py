from rest_framework import serializers
from .models import Book, Author

# 작가 시리얼라이저
class AuthorSrializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

# 책 시리얼라이저
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSrializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'created_date']
        read_only_fields = ['created_date']
        extra_kwargs = {
            'price': {'required': False},
        }