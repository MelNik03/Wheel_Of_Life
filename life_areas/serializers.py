from rest_framework import serializers
from .models import Rating
from .models import LifeArea

class LifeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeArea
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']  # Пользователь будет определяться автоматически

    def validate_name(self, value):
        # Проверяем, что имя сферы не пустое
        if not value.strip():
            raise serializers.ValidationError("Название сферы не может быть пустым.")
        return value

class RatingSerializer(serializers.ModelSerializer):
    life_area_score = serializers.FloatField(read_only=True)

    class Meta:
        model = Rating
        fields = [
            'id', 'life_area', 'satisfaction', 'balance', 'progress', 
            'priority', 'impact', 'life_area_score', 'date'
        ]
        read_only_fields = ['id', 'date', 'life_area_score']

    def validate(self, data):
        # Проверяем, что все оценки находятся в диапазоне от 1 до 5
        for field in ['satisfaction', 'balance', 'progress', 'priority', 'impact']:
            if data[field] < 1 or data[field] > 5:
                raise serializers.ValidationError(f"{field} must be between 1 and 5.")
        return data
