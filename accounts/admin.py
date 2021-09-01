from accounts.models import TradingAccount, TradingAccountTransactions
from django.contrib import admin

# Register your models here.
admin.site.register(TradingAccount)
admin.site.register(TradingAccountTransactions)