from django.urls import path, include
from rest_framework import routers
from tracker import views

router = routers.DefaultRouter()

router.register('habit', views.HabitView, basename='habit')

router.register('habit-log', views.HabitLogView, basename='habit_log')

urlpatterns = [
    path('', include(router.urls)),
]