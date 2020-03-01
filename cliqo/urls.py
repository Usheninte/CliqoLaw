from django.urls import path

from . import views

app_name = 'cliqo'
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('matters', views.MattersListView.as_view(), name="matters"),
    path('new-matter', views.new_matter, name="new-matter"),
]
