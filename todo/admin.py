from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoView(admin.ModelAdmin):

    model = Todo

    list_display = (
        'owner',
        'title',
        'completed',
    )

    list_filter = (
        'owner',
        'completed',
    )

    search_fields = (
        'owner',
        'title',
        'details',
    )

