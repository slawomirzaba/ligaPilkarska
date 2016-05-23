from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from main.models import *
from main.forms import ClubForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_clubs_edit(View):
	def get(self, request, id = None):
		club = get_object_or_404(Club, pk=id)
		form = ClubForm(instance = club)
		return render(request, 'main/tables_management_clubs_edit.html', {'form': form})

	def post(self, request, id = None):
		club = get_object_or_404(Club, pk=id)
		form = ClubForm(request.POST or None, instance=club)
		if form.is_valid():
			form.save()
			return redirect("tables_management_clubs")
		else:
			return render(request, 'main/tables_management_clubs_edit.html', {'form': form})
