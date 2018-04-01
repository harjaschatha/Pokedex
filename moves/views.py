from django.shortcuts import render
from django.http import HttpResponse
from .models import Move


def index(request):
	all_moves = moves.objects.all()
	template = 'moves/index.html'
	context = { 'moves': all_moves }

	return render(request, template, context)