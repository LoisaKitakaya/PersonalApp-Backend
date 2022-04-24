from django.urls import include, path
from todo import views
from rest_framework import routers

# routers

router = routers.DefaultRouter()

router.register('todo', views.TodoViewset, basename='todo')

# urls

urlpatterns = [
    path('', include(router.urls)),
    path('filter-complete/', views.filter_by_complete, name='filter_complete'),
    path('filter-incomplete/', views.filter_by_incomplete, name='filter_incomplete'),
]