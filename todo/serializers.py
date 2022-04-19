from rest_framework import serializers
from todo.models import Tag, Todo

# serializer classes
class TagSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tag

        fields = ['tag']

class TodoSerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:

        model = Todo

        fields = ['title', 'details', 'completed', 'tags']