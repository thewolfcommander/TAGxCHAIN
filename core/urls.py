from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),

    # Miscellaneuous URL patterns
    path('miscellaneous/about/', about, name='about'),
    path('miscellaneous/contact/', contact, name='contact'),
    path('miscellaneous/support/', support, name='support'),

    # Analysis Urls
    path('analysis/screener/crypto/', crypto_screener, name='crypto_screener'),
    path('analysis/screener/forex/', forex_screener, name='forex_screener'),
    path('analysis/screener/stocks/', stock_screener, name='stock_screener'),
]