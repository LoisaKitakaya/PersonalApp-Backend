from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET'])
def filter_by_complete(request):

    completed = Todo.objects.filter(completed=True, owner=request.user)

    serializer = TodoSerializer(completed, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_by_incomplete(request):

    not_completed = Todo.objects.filter(completed=False, owner=request.user)

    serializer = TodoSerializer(not_completed, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)