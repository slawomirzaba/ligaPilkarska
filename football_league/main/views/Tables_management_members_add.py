from django.shortcuts import render, redirect
from django.views.generic import View
from main.models import *
from main.forms import Member_of_gameForm
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_members_add(View):
	def get(self, request):
		form = Member_of_gameForm()
		return render(request, 'main/tables_management_members_add.html', {'form': form})

	def post(self, request):
		form = Member_of_gameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("tables_management_members")
		else:
			return render(request, 'main/tables_management_members_add.html', {'form': form})
