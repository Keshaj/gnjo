#User/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for index page at 127.0.0.1:port/
    path('', views.index, name='index'),

    # URL for login page at 127.0.0.1:port/account
    path('account', views.login_view, name='login'),
]