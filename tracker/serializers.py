from rest_framework import serializers
from tracker.models import Habit, HabitLog

# your serializer here

class HabitSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:

        model = Habit

        fields = [
            'id',
            'created_at',
            'updated_at',
            'owner',
            'title',
            'action',
            'units',
            'goal',
        ]

class HabitLogSerializer(serializers.ModelSerializer):

    habit = serializers.StringRelatedField()

    owner = serializers.StringRelatedField()

    class Meta:

        model = HabitLog

        fields = [
            'id',
            'created_at',
            'updated_at',
            'achievement',
            'habit',
            'owner',
        ]