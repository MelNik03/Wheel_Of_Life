# life_areas/models.py

from django.db import models
from django.contrib.auth.models import User

class LifeArea(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="life_areas")

    def __str__(self):
        return self.name

class Rating(models.Model):
    life_area = models.ForeignKey(LifeArea, on_delete=models.CASCADE, related_name="ratings")
    satisfaction = models.PositiveSmallIntegerField()  # Удовлетворенность
    balance = models.PositiveSmallIntegerField()       # Баланс
    progress = models.PositiveSmallIntegerField()      # Прогресс
    priority = models.PositiveSmallIntegerField()      # Приоритетность
    impact = models.PositiveSmallIntegerField()        # Влияние на жизнь
    date = models.DateField(auto_now_add=True)

    @property
    def life_area_score(self):
        # Вычисляем среднее значение критериев
        return round(
            (self.satisfaction + self.balance + self.progress + self.priority + self.impact) / 5,
            2
        )

    def __str__(self):
        return f"Rating for {self.life_area.name} on {self.date}"

class CalculatedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calculated_data")
    life_area = models.ForeignKey(LifeArea, on_delete=models.CASCADE)
    average_rating = models.FloatField()
    calculated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Avg Rating: {self.average_rating} for {self.life_area.name}"
