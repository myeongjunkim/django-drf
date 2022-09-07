from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Mata:
        model =  Todo
        field =  ('id', 'title', 'description', 'complete', 'important')