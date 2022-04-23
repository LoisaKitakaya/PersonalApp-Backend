from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets

# Create your views here.

# actual classes used in frontend

class TodoViewset(viewsets.ModelViewSet):

    queryset = Todo.objects.all()

    serializer_class = TodoSerializer

    def get_queryset(self):
        
        user = self.request.user

        return self.queryset.filter(owner=user)

    def perform_create(self, serializer):

        user = self.request.user
        
        serializer.save(owner = user)