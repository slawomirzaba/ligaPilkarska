from django.shortcuts import render
from django.views.generic import View

class Tables_management(View):

	def get(self, request):
		return render(request, 'main/tables_management.html')
