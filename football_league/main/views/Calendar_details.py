from django.shortcuts import render
from django.views.generic import View
from main.models import *


class Calendar_details(View):
    def get(self, request, game_id):
        host_members = []
        guest_members = []
        members = Member_of_game.objects.all()
        game = Game.objects.get(id=game_id)
        host_name = game.host.name
        guest_name = game.guest.name

        for member in members:
            if game in member.games.all():
                if host_name == member.member.club.name:
                    host_members.append(member)
                elif guest_name == member.member.club.name:
                    guest_members.append(member)

        return render(request, 'main/calendar_details.html',
                              {'host_name': host_name, 'guest_name': guest_name, 'host_members': host_members,
                               'guest_members': guest_members})
