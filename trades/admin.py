from django.contrib import admin
from trades.forms import TradingDayForm, TradingDayTradeForm

from trades.models import TradingDay, TradingDayTrade


class TradingDayTradeAdminInline(admin.TabularInline):
    model = TradingDayTrade
    extra = 0
    form = TradingDayTradeForm


@admin.register(TradingDay)
class TradingDayAdmin(admin.ModelAdmin):
    """
    Admin settings for trading day
    """
    list_display = ['id', 'date', 'day', 'profit_n_loss', 'charges', 'net_profit_n_loss', 'is_active', 'is_profit']
    list_filter = ['day', 'is_active', 'is_profit', 'created_timestamp', 'updated_timestamp']
    search_fields = ['date', 'day', 'remarks']
    inlines = [TradingDayTradeAdminInline, ]
    form = TradingDayForm


@admin.register(TradingDayTrade)
class TradingDayTradeAdmin(admin.ModelAdmin):
    """
    Admin settings for trading day
    """
    list_display = ['id', 'trading_day', 'position', 'symbol', 'quantity', 'profit_n_loss', 'is_profit']
    list_filter = ['position', 'type_of_trade', 'symbol', 'is_profit', 'is_active', 'created_timestamp', 'updated_timestamp']
    search_fields = ['trading_day__date', 'trading_day__day', 'remarks', 'position', 'symbol', 'title']