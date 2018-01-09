from django.conf.urls import include, url
from django.contrib import admin
from dashboard.views import DashboardView
from django.conf import settings
from django.conf.urls.static import static
from achievement.views import AchievementListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'trek.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #handle dashboard views
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    #Admin View
    url(r'^admin/', include(admin.site.urls)),
    #Registration views
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    #Achievement List View
    url(r'^achievements/$', AchievementListView.as_view(), name='Achievements')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
