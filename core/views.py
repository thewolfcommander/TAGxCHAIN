from django.shortcuts import render
from core.models import Exchange

# Create your views here.
def home(request):
    overview_symbols = [
        "NASDAQ:AAPL",
        "FX:EURUSD",
        "BITSTAMP:BTCUSD"
    ]
    context = {
        'overview_symbols': overview_symbols
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/miscellaneous/about.html')


def contact(request):
    return render(request, 'core/miscellaneous/contact.html')


def support(request):
    return render(request, 'core/miscellaneous/support.html')

# Screeners

def crypto_screener(request):
    """
    View for handling crypto screener
    """
    page_title = "Crypto Screener"
    return render(request, 'core/analysis/crypto_screener.html', {'page_title': page_title})

def forex_screener(request):
    """
    View for handling stock screener
    """
    page_title = "Forex Screener"
    return render(request, 'core/analysis/forex_screener.html', {'page_title': page_title})

def stock_screener(request):
    """
    View for handling stock screener
    """
    page_title = "Stock Screener"
    return render(request, 'core/analysis/stock_screener.html', {'page_title': page_title})


# Analysis
def analysis_market_quotes(request):
    """
    View for handling market quotes
    """
    page_title = "Market Quotes"
    return render(request, 'core/analysis/analysis_market_quotes.html', {'page_title': page_title})

def fundamental_analysis(request):
    """
    View for handling fundamental analysis
    """
    page_title = "Fundamental Analysis"
    symbol = request.GET.get('symbol', None)
    exchange = request.GET.get('exchange', None)
    if symbol is None and exchange is None:
        symbol = 'AAPL'
        exchange = 'NASDAQ'
    else:
        symbol = symbol.upper()
        exchange = exchange.upper()
    exchange_list = Exchange.objects.filter(name=exchange)
    exchange_list_all = Exchange.objects.all()
    print(exchange_list_all)
    if exchange_list.exists():
        context = {'page_title': page_title, 'symbol': symbol, 'exchange': exchange, 'exchanges': exchange_list_all}
    else:
        context = {'page_title': page_title, 'symbol': "RELIANCE", 'exchange': "NSE", 'message': "WRONG Exchange Selected", 'exchanges': exchange_list_all}
    return render(request, 'core/analysis/fundamental_analysis.html', context)

def technical_chart(request):
    """
    View for handling technical chart
    """
    page_title = "Technical Chart"
    return render(request, 'core/analysis/technical_chart.html', {'page_title': page_title})