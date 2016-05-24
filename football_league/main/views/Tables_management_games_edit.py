from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from main.models import *
from main.forms import GameForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_games_edit(View):
	def get(self, request, id = None):
		game = get_object_or_404(Game, pk=id)
		form = GameForm(instance = game)
		return render(request, 'main/tables_management_games_edit.html', {'form': form})

	def post(self, request, id = None):
		game = get_object_or_404(Game, pk=id)
		form = GameForm(request.POST or None, instance=game)
		if form.is_valid():
			form.save()
			return redirect("tables_management_games")
		else:
			return render(request, 'main/tables_management_games_edit.html', {'form': form})
