from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.xpg, name='xpg'),
    path('logout', LogoutView.as_view(), name='logout')
]
