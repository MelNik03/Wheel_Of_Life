from django.urls import path, include
from .views import RatingListCreateView, RatingDetailView, LifeAreaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'life-areas', LifeAreaViewSet, basename='life-area')

urlpatterns = [
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
    path('api/', include(router.urls)),
]