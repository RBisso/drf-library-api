from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "isbn13",
            "publish_date",
            "price",
        ]
        extra_kwargs = {
            "publish_date": {"required": False},
            "price": {"required": False},
            "isbn13": {"required":False}
        }