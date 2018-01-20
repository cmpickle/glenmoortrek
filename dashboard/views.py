from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from achievement.models import Achievement

# Create your views here.

class DashboardView(ListView):
	model = Achievement
	template_name = "dashboard/view.html"

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)
		return context