from tracker.models import Habit, HabitLog
from tracker.serializers import HabitSerializer, HabitLogSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User

# Create your views here.

# tracker class views
class HabitView(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
    ]

    queryset = Habit.objects.all()

    serializer_class = HabitSerializer

    def get_queryset(self):
        
        user = self.request.user

        return self.queryset.filter(owner = user)

    def perform_create(self, serializer):
        
        user = self.request.user

        serializer.save(owner = user)

class HabitLogView(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
    ]

    queryset = HabitLog.objects.all()

    serializer_class = HabitLogSerializer

    def get_queryset(self):
        
        user = self.request.user

        return self.queryset.filter(owner = user)

    def perform_create(self, serializer):
        
        user = self.request.user

        serializer.save(owner = user)