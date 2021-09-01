from django.shortcuts import render
from core.models import Exchange
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

@login_required
def about(request):
    return render(request, 'core/miscellaneous/about.html')

@login_required
def contact(request):
    return render(request, 'core/miscellaneous/contact.html')

@login_required
def support(request):
    return render(request, 'core/miscellaneous/support.html')

# Screeners
@login_required
def crypto_screener(request):
    """
    View for handling crypto screener
    """
    page_title = "Crypto Screener"
    return render(request, 'core/analysis/crypto_screener.html', {'page_title': page_title})

@login_required
def forex_screener(request):
    """
    View for handling stock screener
    """
    page_title = "Forex Screener"
    return render(request, 'core/analysis/forex_screener.html', {'page_title': page_title})

@login_required
def stock_screener(request):
    """
    View for handling stock screener
    """
    page_title = "Stock Screener"
    return render(request, 'core/analysis/stock_screener.html', {'page_title': page_title})


# Analysis
@login_required
def analysis_market_quotes(request):
    """
    View for handling market quotes
    """
    page_title = "Market Quotes"
    return render(request, 'core/analysis/analysis_market_quotes.html', {'page_title': page_title})

@login_required
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

@login_required
def technical_chart(request):
    """
    View for handling technical chart
    """
    page_title = "Technical Chart"
    return render(request, 'core/analysis/technical_chart.html', {'page_title': page_title})

@login_required
def forex_cross_rates(request):
    """
    View for handling technical chart
    """
    page_title = "Forex Cross Rates"
    return render(request, 'core/analysis/forex_cross_rates.html', {'page_title': page_title})

@login_required
def forex_heat_map(request):
    """
    View for handling technical chart
    """
    page_title = "Forex Heat Map"
    return render(request, 'core/analysis/forex_heat_map.html', {'page_title': page_title})

@login_required
def symbol_overview(request):
    """
    View for handling technical chart
    """
    page_title = "Symbol Overview"
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
    return render(request, 'core/analysis/symbol_overview.html', context)


@login_required
def technical_analysis(request):
    """
    View for handling technical analysis
    """
    page_title = "Technical Analysis"
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
    return render(request, 'core/analysis/technical_analysis.html', context)