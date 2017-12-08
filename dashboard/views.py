from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class DashboardView(View):
	def get(self, request, *args, **kwargs):
		# curated = CuratedProducts.objects.filter(active=True).order_by("?")

		context = {
		# 	"curated": curated,
		}
		return render(request, "dashboard/view.html", context)