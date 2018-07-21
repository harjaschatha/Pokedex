from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from .helpers import generate_defenses

def index(request):  # This is the test case where the opening Pokedex page will show
    all_pokemon = Pokemon.objects.all()
    template = 'pokedex/index.html'
    context = { 'pokemons': all_pokemon }

    return render(request, template, context)


def detail(request, dex):
    # return HttpResponse('<h1>{}</h1>'.format(dex))
    pokemon = Pokemon.objects.get(dex__exact=dex)
    try:
    	type1, type2 = pokemon.types.split('/')
    except ValueError:
    	type1 = pokemon.types
    	type2 = ''
    defenses = generate_defenses(type1, type2)
    template = 'pokedex/detail.html'
    context = { 'pokemon': pokemon, 'defenses': defenses}
    	
    return render(request, template, context)
