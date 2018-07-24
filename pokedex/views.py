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
    
    print(defenses)
    len_list = []
    for value in defenses.values():
        len_list.append(len(value))
    max_len = max(len_list)

    for value in defenses.values():
        if len(value) < max_len:
            diff = max_len - len(value)
            for _ in range(diff):
                value.append('-')
            

    defenses_new = {}
    for key in defenses.keys():
        if key == '0.0':
            defenses_new['Immune'] = defenses[key]
        elif key == '0.25':
            defenses_new['Not Very Effective (1/4)'] = defenses[key]
        elif key == '0.5':
            defenses_new['Not Very Effective (1/2)'] = defenses[key]    
        elif key == '1.0':
            defenses_new['Neutral'] = defenses[key]
        elif key == '2.0':    
            defenses_new['Super Effective (2)'] = defenses[key]
        elif key == '4.0':
            defenses_new['Super Effective (4)'] = defenses[key]                                               
 

    template = 'pokedex/detail.html'
    context = { 'pokemon': pokemon, 'defenses': defenses_new }
    	
    return render(request, template, context)
