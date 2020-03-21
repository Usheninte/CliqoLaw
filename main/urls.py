from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('signup', views.signup_page, name="signup"),
    path('accounts/login/', views.login_page, name="login"),
    path('logout', views.logout_user, name="logout")
]
