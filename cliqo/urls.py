from django.urls import path

from . import views

app_name = 'cliqo'
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
]