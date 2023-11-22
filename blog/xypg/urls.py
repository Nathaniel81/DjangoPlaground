from django.urls import path
# from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback'),
    # path('logout', LogoutView.as_view(), name='logout')
]