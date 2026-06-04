from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PokemonViewSet, TrainerViewSet

router = DefaultRouter()
router.register(r"pokemons", PokemonViewSet)
router.register(r"trainers", TrainerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]