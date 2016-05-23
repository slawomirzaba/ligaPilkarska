from django.shortcuts import render
from django.views.generic import View
from main.models import *

class Tables_management_members(View):
	def get(self, request):
		members = Member_of_game.objects.all()
		return render(request, 'main/tables_management_members.html', {'members': members})
