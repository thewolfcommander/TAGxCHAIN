from django.db import models
from django.contrib.auth.models import User

class TradingAccount(models.Model):
    """
    Data for trading account handling
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo_money = models.DecimalField(default=50000.00, decimal_places=2, max_digits=20)
    real_money = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    no_of_trades = models.IntegerField(default=0)
    no_of_sessions = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_spam = models.BooleanField(default=False)
    is_bot_account = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.id)}-{str(self.user.username)}"

    
class TradingAccountTransactions(models.Model):
    """
    Data for trading account transactions
    """
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    is_inbound = models.BooleanField(default=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_correct = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.id)}-{str(self.account.user.username)}"