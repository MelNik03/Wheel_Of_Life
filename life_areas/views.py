from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Rating, LifeArea
from .serializers import RatingSerializer
from rest_framework.views import exception_handler

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        life_area = serializer.validated_data.get('life_area')
        if life_area.user != self.request.user:
            raise NotFound("LifeArea not found or does not belong to the user.")
        rating = serializer.save()
        # Дополнительно можно логировать вычисленный life_area_score, если требуется
        print(f"Calculated life_area_score: {rating.life_area_score}")

class RatingDetailView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        # Фильтрация оценок по текущему пользователю
        return Rating.objects.filter(life_area__user=self.request.user)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response