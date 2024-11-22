# life_areas/admin.py

from django.contrib import admin
from .models import LifeArea, Rating, CalculatedData

admin.site.register(LifeArea)
admin.site.register(Rating)
admin.site.register(CalculatedData)
