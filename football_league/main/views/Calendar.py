from django.shortcuts import render
from django.views.generic import View
from main.models import *
from main.views.Home import Game_details

class Calendar(View):
    def get(self, request):
        games = Game.objects.all()
        goal_events = Event.objects.filter(type__type__icontains="Gol")
        results = []
        for game in games:
            tmp = Game_details()
            tmp.id = game.id
            tmp.data = game.date
            tmp.queue = game.number_of_queue
            tmp.host_name = game.host.name
            tmp.guest_name = game.guest.name
            for event in goal_events:
                if event.person.club.name == tmp.host_name \
						and event.game.host.name == tmp.host_name and event.game.guest.name == tmp.guest_name:
                    tmp.host_goals += 1
                elif event.person.club.name == tmp.guest_name \
					and event.game.host.name == tmp.host_name and event.game.guest.name == tmp.guest_name:
                    tmp.guest_goals += 1
            results.append(tmp)

        return render(request, 'main/calendar.html', dict(results=results))
