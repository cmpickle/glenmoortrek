from django.conf.urls import include, url
from django.contrib import admin
from dashboard.views import DashboardView

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
]
