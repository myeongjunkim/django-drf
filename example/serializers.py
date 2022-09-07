from rest_framework import serializers
from .models import *


# ModelSerializer 기본 형태
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description',]
