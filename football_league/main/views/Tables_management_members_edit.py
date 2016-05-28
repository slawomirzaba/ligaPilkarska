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
		message = ''
		matches = list()

		if form.is_valid():
			member = form.cleaned_data['member']
			games = form.cleaned_data['games']
			for game in games:
				host = game.host
				guest = game.guest
				if member.club != host and member.club != guest:
					matches.append('{0} - {1}'.format(host.name, guest.name))
			if matches:
				message = 'Wybrany uczestnik nie nalezy do zadnej z druzyn meczu:'
				for match in matches:
					message += ' {},'.format(match)
				message = message[0: -1]
				return render(request, 'main/tables_management_members_edit.html', {'form': form, 'error': message})
			form.save()
			return redirect("tables_management_members")
		else:
			return render(request, 'main/tables_management_members_edit.html', {'form': form})
