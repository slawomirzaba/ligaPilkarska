from django.shortcuts import render
from django.views.generic import View
from main.models import *

class Tables_management_members(View):
	def get(self, request):
		search_query = request.GET.get('search_box', None)
		members = Member_of_game.objects.all()

		if search_query:
			members = Member_of_game.objects.filter(member__surname__icontains=search_query) \
					  | Member_of_game.objects.filter(member__name__icontains=search_query)

		return render(request, 'main/tables_management_members.html', {'members': members})
