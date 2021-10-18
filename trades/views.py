from django.shortcuts import render
from trades.helpers import calculate_total_pnl
from trades.models import *

# Create your views here.
def trades_overview(request):
    trades = TradingDay.objects.filter(user=request.user).order_by('-created_timestamp')
    pnl, percent = calculate_total_pnl(request.user)
    context = {
        'trades': trades,
        'stats': {
            'trade_count': trades.count(),
            'total_pnl': pnl,
            'total_per': percent
        }
    }
    return render(request, 'trades/trades_overview.html', context)


def add_trade(request):
    return render(request, 'trades/add_trade.html')