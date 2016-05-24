from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from main.models import *
from main.views.Tables_management_clubs import Tables_management_clubs

class Tables_management_games_delete(View):

    def post(self, request, id = None):
        game = Game.objects.get(id=id)
        game.delete()
        return redirect("tables_management_games")
