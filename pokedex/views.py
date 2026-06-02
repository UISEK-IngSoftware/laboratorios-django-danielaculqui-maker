from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from pokedex.forms import PokemonForm
from django.shortcuts import render, redirect, get_object_or_404
from pokedex.forms import PokemonForm, TrainerForm
from django.contrib import messages

from django.contrib import messages

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    
    if request.user.is_authenticated:
        messages.success(request, f'¡Bienvenido, {request.user.username}!')
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons, 
        'trainers': trainers}, 
        request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    
    return HttpResponse(template.render(context, request))
def trainer(request, id: int):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))
@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})
@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})
@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokedex:index')

    return render(request, 'delete_pokemon.html', {
        'pokemon': pokemon
    })
    
class CustomLoginView(LoginView):
    template_name = "login_form.html"

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    pokemons_afectados = Pokemon.objects.filter(trainer=trainer)
    if request.method == 'POST':
        trainer.delete()
        return redirect('pokedex:index')
    return render(request, 'delete_trainer.html', {
        'trainer': trainer,
        'pokemons_afectados': pokemons_afectados
    })