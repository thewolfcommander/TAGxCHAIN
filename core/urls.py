from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),

    # Miscellaneuous URL patterns
    path('miscellaneous/about/', about, name='about'),
    path('miscellaneous/contact/', contact, name='contact'),
    path('miscellaneous/support/', support, name='support'),
]