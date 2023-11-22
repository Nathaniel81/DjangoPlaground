from django.urls import path
from .views import payment_link_view, intx

urlpatterns = [
    path('', intx),
    path('pay-with-yenepay/', payment_link_view, name='payment_link'),
]