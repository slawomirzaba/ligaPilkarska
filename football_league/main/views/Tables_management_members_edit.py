from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from main.models import *
from main.forms import Member_of_gameForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_members_edit(View):
	def get(self, request, id = None):
		member = get_object_or_404(Member_of_game, pk=id)
		form = Member_of_gameForm(instance = member)
		return render(request, 'main/tables_management_members_edit.html', {'form': form})

	def post(self, request, id = None):
		member = get_object_or_404(Member_of_game, pk=id)
		form = Member_of_gameForm(request.POST or None, instance=member)
		if form.is_valid():
			form.save()
			return redirect("tables_management_members")
		else:
			return render(request, 'main/tables_management_members_edit.html', {'form': form})
