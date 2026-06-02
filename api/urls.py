from django.urls import path, include
from rest_framework import routers
from .views import PokemonViewSet

router = routers.DefaultRouter()
router.register(r"pokemons", PokemonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]