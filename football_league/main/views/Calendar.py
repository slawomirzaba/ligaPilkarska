from django.shortcuts import render
from django.views.generic import View

class Calendar(View):

	def get(self, request):
		return render(request, 'main/calendar.html')
