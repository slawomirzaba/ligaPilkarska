from django.shortcuts import render
from django.views.generic import View
from main.models import *

class Tables_management_clubs(View):
	def get(self, request):
		clubs = Club.objects.all()
		return render(request, 'main/tables_management_clubs.html', {'clubs': clubs})
