from django.shortcuts import render
from django.views.generic import View
from main.models import *

class Tables_management_games(View):
	def get(self, request):
		games = Game.objects.all()
		return render(request, 'main/tables_management_games.html', {'games': games})
