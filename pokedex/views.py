from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon


def index(request):  # This is the test case where the opening Pokedex page will show
    all_pokemon = Pokemon.objects.all()
    template = 'pokedex/index.html'
    context = { 'pokemons': all_pokemon }

    return render(request, template, context)


def detail(request, dex):
    # return HttpResponse('<h1>{}</h1>'.format(dex))
    pokemon = Pokemon.objects.get(dex__exact=dex)
    template = 'pokedex/detail.html'
    context = { 'pokemon': pokemon }

    return render(request, template, context)
