from django.http import HttpResponse
from django.views.generic import ListView
from achievement.models import Achievement

# Create your views here.
class AchievementListView(ListView):
    model = Achievement

    template_name = 'AchievementListView.html'

    def get_context_data(self, **kwargs):
        context = super(AchievementListView, self).get_context_data(**kwargs)
        
        return context