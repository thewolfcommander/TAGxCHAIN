from django.urls import path

from .views import *

app_name = 'trades'

urlpatterns = [
    path('overview/', trades_overview, name='trades_overview'),
    path('add/', add_trade, name='add_trade'),
]