from django.contrib import admin
from tracker.models import Habit, HabitLog

# Register your models here.
@admin.register(Habit)
class HabitView(admin.ModelAdmin):

    model = Habit

    list_display = (
        'owner',
        'title',
        'action',
        'units',
    )

    list_filter = (
        'owner',
    )

    search_fields = (
        'owner',
        'title',
        'action',
        'units',
        'goals',
    )

@admin.register(HabitLog)
class LogView(admin.ModelAdmin):

    model = HabitLog

    list_display = (
        'date',
        'achievement',
        'habit',
        'owner',
    )

    list_filter = (
        'date',
        'habit',
        'owner',
    )

    search_fields = (
        'date',
        'achievement',
        'habit',
        'owner',
    )