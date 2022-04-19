from django.shortcuts import render
from todo.models import Tag, Todo
from todo.serializers import TagSerializer, TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def view_tags(request):

    tags = Tag.objects.all()

    serializer = TagSerializer(tags, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_todo(request):

    todo = Todo.objects.all()

    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)