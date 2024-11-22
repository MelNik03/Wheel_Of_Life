# life_areas/services.py

from django.db.models import Avg
from .models import LifeArea, Rating, CalculatedData

def calculate_diagram_data(user):
    life_areas = LifeArea.objects.filter(user=user)
    total_avg = 0
    total_count = 0

    for area in life_areas:
        avg_rating = area.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
        total_avg += avg_rating
        total_count += 1

        # Сохранение данных для построения диаграммы по каждому полю
        CalculatedData.objects.update_or_create(
            user=user, life_area=area,
            defaults={'average_rating': avg_rating}
        )

    # Рассчёт и сохранение общего среднего значения
    overall_average = total_avg / total_count if total_count > 0 else 0
    return overall_average
