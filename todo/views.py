from todo.models import Tag, Todo
from todo.serializers import TagSerializer, TodoSerializer
from rest_framework import viewsets

# Create your views here.

# actual classes used in frontend

class TagViewset(viewsets.ModelViewSet):

    queryset = Tag.objects.all()

    serializer_class = TagSerializer

    def get_queryset(self):

        return self.queryset

class TodoViewset(viewsets.ModelViewSet):

    queryset = Todo.objects.all()

    serializer_class = TodoSerializer

    def get_queryset(self):
        
        user = self.request.user

        return self.queryset.filter(owner=user)

    def perform_create(self, serializer):

        user = self.request.user
        
        serializer.save(owner = user)