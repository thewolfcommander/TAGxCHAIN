from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/miscellaneous/about.html')


def contact(request):
    return render(request, 'core/miscellaneous/contact.html')


def support(request):
    return render(request, 'core/miscellaneous/support.html')