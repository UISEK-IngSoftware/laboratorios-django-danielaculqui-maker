from django.shortcuts import render
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from rest_framework.permissions import IsAuthenticated, AllowAny
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        from .serializers import PokemonSerializer
        return PokemonSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        from .serializers import TrainerSerializer
        return TrainerSerializer