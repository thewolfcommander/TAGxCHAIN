from django.shortcuts import render

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
def analysis_ticker(request):
    """
    View for handling ticker
    """
    page_title = "Ticker"
    return render(request, 'core/analysis/analysis_ticker.html', {'page_title': page_title})