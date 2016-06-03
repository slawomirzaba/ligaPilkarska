from django.shortcuts import render
from django.views.generic import View
from main.models import *


class Calendar_details(View):
    def get(self, request, game_id):
        host_members = []
        guest_members = []
        game = Game.objects.get(id=game_id)
        members = Member_of_game.objects.filter(member__club__id=game.host.id) \
					  | Member_of_game.objects.filter(member__club__id=game.guest.id)
        host_name = game.host.name
        guest_name = game.guest.name
        role = Roles_in_game.objects.get(role='Pilkarz')
        for member in members:
            if game in member.games.all():
                if host_name == member.member.club.name and role in member.roles.all():
                    host_members.append(member)
                elif guest_name == member.member.club.name and role in member.roles.all():
                    guest_members.append(member)

        return render(request, 'main/calendar_details.html',
                              {'host_name': host_name, 'guest_name': guest_name, 'host_members': host_members,
                               'guest_members': guest_members})
