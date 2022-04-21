from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('todo-api/', include('todo.urls')),
    path('tracker-api/', include('tracker.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

admin.site.site_header = 'Personal App Admin Panel'
admin.site.site_title = 'Personal App Backend'
