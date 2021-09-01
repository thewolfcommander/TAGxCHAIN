from django.shortcuts import render,redirect
from .forms import EditUserForm, LoginForm, NewUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import TradingAccount


def logout(request):
    """
    View for handling logout requests
    """
    auth_logout(request)
    return redirect('accounts:login')


def login(request):
    """
    View for handling login requests
    """
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                redirect_path = request.GET.get('next', '/')
                return redirect(redirect_path)
            else:
                messages.error(request,"You are not registered.")
        else:
            messages.error(request,"Invalid username or password.")
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    """
    View for handling register requests
    """
    if request.method == 'POST':
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful." )
            try:
                trading_account = TradingAccount.objects.create(
                    user=user
                )
            except Exception as e:
                print(e)
                messages.error(request, e)
            return redirect("core:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)

@login_required
def my_account(request):
    """
    View for handling my account
    """
    return render(request, 'accounts/my_account.html')