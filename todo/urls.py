from django.urls import path
from todo import views

urlpatterns = [
    path('tags/', views.view_tags),
    path('todo/', views.view_todo),
]