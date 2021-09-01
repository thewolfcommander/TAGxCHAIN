from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),

    # Miscellaneuous URL patterns
    path('miscellaneous/about/', about, name='about'),
    path('miscellaneous/contact/', contact, name='contact'),
    path('miscellaneous/support/', support, name='support'),

    # Screener Urls
    path('screener/crypto/', crypto_screener, name='crypto_screener'),
    path('screener/forex/', forex_screener, name='forex_screener'),
    path('screener/stocks/', stock_screener, name='stock_screener'),

    # Analysis Urls
    path('analysis/market-quotes/', analysis_market_quotes, name='analysis_market_quotes'),
    path('analysis/fundamental-analysis/', fundamental_analysis, name='fundamental_analysis'),
]