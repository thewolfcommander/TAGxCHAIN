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