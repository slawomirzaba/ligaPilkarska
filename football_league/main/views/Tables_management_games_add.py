from django.shortcuts import render, redirect
from django.views.generic import View
from main.models import *
from main.forms import GameForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_games_add(View):
	def get(self, request):
		form = GameForm()
		return render(request, 'main/tables_management_games_add.html', {'form': form})

	def post(self, request):
		form = GameForm(request.POST)
		message = ''

		if form.is_valid():
			host = form.cleaned_data['host']
			guest = form.cleaned_data['guest']
			queue = form.cleaned_data['number_of_queue']
			proper_game = [game for game in Game.objects.all() if game.host == host and game.guest == guest]
			converted_squads = [game for game in Game.objects.all() if game.host == guest and game.guest == host]
						
			if host == guest:
				message = 'Blad! Pola gospodarza i goscia musza byc rozne!'
				return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})
			
			elif proper_game:
				message = "Blad! Istnieje juz taki mecz w lidze"
				return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})

			elif converted_squads:
				game = converted_squads[0]
				if queue == game.number_of_queue:
					message = "Blad! Niewlasciwy numer kolejki dla meczu!"
					return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})

			form.save()
			return redirect("tables_management_games")
		else:
			return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})
