from django.shortcuts import render

# Create your views here.
def trades_overview(request):
    return render(request, 'trades/trades_overview.html')


def add_trade(request):
    return render(request, 'trades/add_trade.html')