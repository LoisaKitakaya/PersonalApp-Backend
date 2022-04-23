from rest_framework import serializers
from todo.models import Todo

# serializer classes

class TodoSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:

        model = Todo

        fields = [
            'id',
            'owner',
            'title',
            'details',
            'completed',
            'tags'
        ]
