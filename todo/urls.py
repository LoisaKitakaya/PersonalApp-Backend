from django.urls import include, path
from todo import views
from rest_framework import routers

# routers

router = routers.DefaultRouter()

router.register('tags', views.TagViewset, basename='tags')

router.register('todo', views.TodoViewset, basename='todo')

# urls

urlpatterns = [
    path('', include(router.urls)),
]