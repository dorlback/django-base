from rest_framework import serializers
from .models import Book, Author
from drf_writable_nested.serializers import WritableNestedModelSerializer

# 작가 시리얼라이저
class AuthorSrializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

# 책 시리얼라이저
class BookSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    author = AuthorSrializer()
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'price', 'created_date']
        read_only_fields = ['pk', 'created_date']
        extra_kwargs = {
            'price': {'required': False},
        }