from django.contrib import admin

from trades.models import TradingDay, TradingDayTrade

# Register your models here.
admin.site.register(TradingDay)
admin.site.register(TradingDayTrade)