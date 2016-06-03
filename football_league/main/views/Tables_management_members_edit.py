from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from main.models import *
from main.forms import Member_of_game_edit_Form

class Tables_management_members_edit(View):
	def get(self, request, id = None):
		my_member = get_object_or_404(Member_of_game, pk=id)
		form = Member_of_game_edit_Form(instance = my_member)
		return render(request, 'main/tables_management_members_edit.html', {'form': form, 'my_member': my_member})

	def post(self, request, id = None):
		my_member = get_object_or_404(Member_of_game, pk=id)
		form = Member_of_game_edit_Form(request.POST or None, instance=my_member)
		message = ''
		matches = list()

		if form.is_valid():
			games = form.cleaned_data['games']
			member = my_member.member
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
				return render(request, 'main/tables_management_members_edit.html', {'form': form, 'error': message, 'my_member': my_member})
			form.save()
			return redirect("tables_management_members")
		else:
			return render(request, 'main/tables_management_members_edit.html', {'form': form, 'my_member': my_member})
