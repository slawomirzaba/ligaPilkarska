from django.shortcuts import render
from django.views.generic import View
from main.models import *

class Club_details:
    def __init__(self):
        self.club_name = ""
        self.goals_scored = 0
        self.goals_lost = 0
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.points = 0
        self.games = 0

class Game_details:
    def __init__(self):
        self.queue = 0
        self.host_name = ""
        self.guest_name = ""
        self.host_goals = 0
        self.guest_goals = 0
        self.data = ""
        self.id = 0

class Home(View):
    def get(self, request):
        clubs = Club.objects.all()
        games = Game.objects.all()
        events = Event.objects.all()
        results = []
        club_table_results = []
        for game in games:
            tmp = Game_details()
            tmp.id = game.id
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

        for club in clubs:
            tmp_club = Club_details()
            tmp_club.club_name = club.name
            for result in results:
                if result.host_name == tmp_club.club_name:
                    tmp_club.goals_scored += result.host_goals
                    tmp_club.goals_lost += result.guest_goals
                    if result.host_goals > result.guest_goals:
                        tmp_club.wins += 1
                    elif result.host_goals == result.guest_goals:
                        tmp_club.draws += 1
                    else:
                        tmp_club.loses += 1
                elif result.guest_name == tmp_club.club_name:
                    tmp_club.goals_scored += result.guest_goals
                    tmp_club.goals_lost += result.host_goals
                    if result.host_goals < result.guest_goals:
                        tmp_club.wins += 1
                    elif result.host_goals == result.guest_goals:
                        tmp_club.draws += 1
                    else:
                        tmp_club.loses += 1
            tmp_club.points = tmp_club.wins * 3 + tmp_club.draws
            tmp_club.games = tmp_club.wins + tmp_club.draws + tmp_club.loses
            club_table_results.append(tmp_club)

            sortType = request.GET.get("sortType", 'points')
            sortReverse = request.GET.get("sortReverse", 'True')
            print sortType
            if sortType == 'points' and sortReverse == 'True':
                club_table_results = sorted(club_table_results, key=lambda x: x.points, reverse=True)
            elif sortType == 'points' and sortReverse == 'False':
                club_table_results = sorted(club_table_results, key=lambda x: x.points, reverse=False)
            if sortType == 'goals_scored' and sortReverse == 'True':
                club_table_results = sorted(club_table_results, key=lambda x: x.goals_scored, reverse=True)
            elif sortType == 'goals_scored' and sortReverse == 'False':
                club_table_results = sorted(club_table_results, key=lambda x: x.goals_scored, reverse=False)
            if sortType == 'goals_lost' and sortReverse == 'True':
                club_table_results = sorted(club_table_results, key=lambda x: x.goals_lost, reverse=True)
            elif sortType == 'goals_lost' and sortReverse == 'False':
                club_table_results = sorted(club_table_results, key=lambda x: x.goals_lost, reverse=False)

        return render(request, 'main/home.html', dict(club_table_results=club_table_results))

