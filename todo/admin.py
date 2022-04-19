from django.contrib import admin
from .models import Tag, Todo

# Register your models here.
@admin.register(Tag)
class TagView(admin.ModelAdmin):

    model = Tag

    prepopulated_fields = {
        "slug": (
            "tag",
        )
    }

@admin.register(Todo)
class TodoView(admin.ModelAdmin):

    model = Todo

    list_display = (
        'title',
        'completed',
    )

    list_filter = (
        'completed',
    )

    search_fields = (
        'title',
        'details',
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

