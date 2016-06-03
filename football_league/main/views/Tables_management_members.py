from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import *

class Tables_management_members(View):
	def get(self, request):
		search_query = request.GET.get('search_box', "")
		list_members = Member_of_game.objects.filter(member__surname__icontains=search_query) \
					  | Member_of_game.objects.filter(member__name__icontains=search_query)
		paginator = Paginator(list_members, 10)
		page = request.GET.get('page')
		try:
			members = paginator.page(page)
		except PageNotAnInteger:
			members = paginator.page(1)
		except EmptyPage:
			members = paginator.page(paginator.num_pages)

		return render(request, 'main/tables_management_members.html', {'members': members, 'search_query':search_query})
