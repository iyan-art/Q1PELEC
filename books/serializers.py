from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "rating",
            "is_featured",
        ]

    def validate_rating(self, value):
        # Keep it flexible but validate it's a float-like number.
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise serializers.ValidationError("Rating must be a number.")
        return value

