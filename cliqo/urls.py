from django.urls import path

from . import views

app_name = 'cliqo'
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('matters', views.MattersListView.as_view(), name="matters"),
    path('create-matter', views.new_matter, name="new-matter"),
    path('delete-matter/<int:pk>', views.MattersDeleteView.as_view(), name="delete-matter"),
    # path('update-matter/<int:pk>', views.MattersUpdateView.as_view(), name="update-matter"),
    path('main/mtr-<int:pk>', views.MattersHeaderView.as_view(), name="matter-focus"),
    path('create-client', views.new_client, name="new-client"),
    path('create-collaborator', views.new_collaborator, name="new-collaborator"),
]
