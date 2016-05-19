from django.shortcuts import render
from django.views.generic import View
from main.models import *
from main.forms import ClubForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_clubs_add(View):
	def get(self, request):
		form = ClubForm()
		return render(request, 'main/tables_management_clubs_add.html', {'form': form})

	def post(self, request):
		form = ClubForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/tables_management_clubs.html', {'clubs':Club.objects.all()})
		else:
			return render(request, 'main/tables_management_clubs_add.html', {'form': form})
