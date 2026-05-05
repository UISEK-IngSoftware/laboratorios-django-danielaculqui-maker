from django.http import HttpResponse
from django.template import loader

def index(request):
    pokemons = ['charmander', 'pikachu', 'squirtle']
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon):
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))