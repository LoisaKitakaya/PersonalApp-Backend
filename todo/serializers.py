from rest_framework import serializers
from todo.models import Tag, Todo
from django.contrib.auth.models import User

# serializer classes

class TagSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tag

        fields = [
            'tag'
        ]

class TodoSerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField()

    owner = serializers.StringRelatedField()

    class Meta:

        model = Todo

        fields = [
            'owner',
            'title',
            'details',
            'completed',
            'tags'
        ]
