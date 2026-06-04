from django.shortcuts import render
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()

    def get_serializer_class(self):
        from . serializers import PokemonSerializer
        return PokemonSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()

    def get_serializer_class(self):
        from . serializers import TrainerSerializer
        return TrainerSerializer