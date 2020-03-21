from django.urls import path

from . import views

app_name = 'cliqo'
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('matters', views.MattersListView.as_view(), name="matters"),
    path('create-matter', views.CreateMatterMain.as_view(), name="create-matter"),
    path('main/mtr-<int:pk>', views.MattersMainView.as_view(), name="matter-focus"),
    path('delete-matter/<int:pk>', views.MattersDeleteView.as_view(), name="delete-matter"),
    path('update-matter/<int:pk>', views.MattersUpdateView.as_view(), name="update-matter"),
    path('contacts', views.ContactsListView.as_view(), name="contacts"),
    path('create-contact', views.CreateContactMain.as_view(), name="create-contact"),
    path('main/contact-<int:pk>', views.ContactsMainView.as_view(), name="contact-focus"),
    path('update-contact/<int:pk>', views.ContactsUpdateView.as_view(), name="update-contact"),
    path('main/billings', views.TasksBillingView.as_view(), name="billings")
]
