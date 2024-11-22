from django.urls import path
from .views import RatingListCreateView, RatingDetailView

urlpatterns = [
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
]
