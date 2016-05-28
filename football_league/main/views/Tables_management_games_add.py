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
			if host == guest:
				message = 'Blad! Pola gospodarza i goscia musza byc rozne!'
				return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})
			form.save()
			return redirect("tables_management_games")
		else:
			return render(request, 'main/tables_management_games_add.html', {'form': form, 'error': message})
