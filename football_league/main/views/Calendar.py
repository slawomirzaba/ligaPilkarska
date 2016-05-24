from django.shortcuts import render
from django.views.generic import View
from main.models import *


class Game_details:
    def __init__(self):
        self.queue = 0
        self.host_name = ""
        self.guest_name = ""
        self.host_goals = 0
        self.guest_goals = 0
        self.data = ""


class Calendar(View):
    def get(self, request):
        games = Game.objects.all()
        events = Event.objects.all()
        results = []
        for game in games:
            tmp = Game_details()
            tmp.data = game.date
            tmp.queue = game.number_of_queue
            tmp.host_name = game.host.name
            tmp.guest_name = game.guest.name
            for event in events:
                if event.type.type == 'Gol' and event.person.club.name == tmp.host_name \
						and event.game.host.name == tmp.host_name and event.game.guest.name == tmp.guest_name:
                    tmp.host_goals += 1
                elif event.type.type == 'Gol' and event.person.club.name == tmp.guest_name \
					and event.game.host.name == tmp.host_name and event.game.guest.name == tmp.guest_name:
                    tmp.guest_goals += 1
            results.append(tmp)

        return render(request, 'main/calendar.html', dict(results=results))
