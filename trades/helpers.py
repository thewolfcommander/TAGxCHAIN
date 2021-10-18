from trades.models import *

def calculate_total_pnl(user):
    pnl = 0.00
    percent = 0.00
    for i in TradingDay.objects.filter(is_front=True, user=user):
        if i.is_profit:
            pnl = pnl + float(i.net_profit_n_loss)
            percent = percent + float(i.pnl_percentage)
        else:
            pnl = pnl - float(i.net_profit_n_loss)
            percent = percent - float(i.pnl_percentage)
    return pnl, percent