import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.
class TradingDay(models.Model):
    """
    Model to handle all the trading day
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who did trade")
    date = models.DateField(default='2000-10-10', help_text="Date on which User traded")
    day = models.CharField(null=True, blank=True, max_length=20, help_text="Day on which User Traded")
    
    profit_n_loss = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Profit/Loss")
    charges = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Broker Charges etc.", null=True)
    net_profit_n_loss = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Net Profit/Loss after Charges")
    amount_used = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Trading amount used")
    pnl_percentage = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, help_text="Percentage of Profit and loss")
    remarks = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=False, help_text="Active only in Swing Trades")
    is_front = models.BooleanField(default=True, help_text="If true, it means trades done after development of this platform.")
    is_profit = models.BooleanField(default=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.id)}-{str(self.user)}"

    
class TradingDayTrade(models.Model):
    """
    Model to handle individual trades for each day
    """
    POSITION_CHOICES = [
        ('Short', 'Short'),
        ('Long', 'Long')
    ]
    TYPE_OF_TRADES = [
        ('Equity', 'Equity'),
        ('Futures', 'Futures'),
        ('Options', 'Options'),
        ('Forex', 'Forex'),
        ('Crypto', 'Crypto'),
        ('Other', 'Other')
    ]
    trading_day = models.ForeignKey(TradingDay, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, null=True, blank=True, choices=POSITION_CHOICES, default='Short', help_text="Position you took - Short/Long")
    type_of_trade = models.CharField(max_length=255, null=True, blank=True, choices=TYPE_OF_TRADES, default='Equity', help_text="Position you took - Short/Long")
    symbol = models.CharField(max_length=255, null=True, blank=True, help_text="Instrument Symbol e.g., SBIN ")
    title = models.CharField(max_length=255, null=True, blank=True, help_text="Intrument Name e.g., State bank of India")
    quantity = models.IntegerField(default=0, help_text="Quantity placed in trade")
    buy_price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Price at which instrument bought")
    sell_price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Price at which instrument sold")
    expected_target = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Target Price")
    stop_loss = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Stop Loss")
    profit_n_loss = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, help_text="Profit/Loss")
    remarks = models.TextField(null=True, blank=True)

    is_intraday = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False, help_text="Active only in Swing Trades")
    is_profit = models.BooleanField(default=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.id)}-{str(self.trading_day.id)}-{str(self.trading_day.user)}"

    
def trading_day_receiver(sender, instance, *args, **kwargs):
    if not instance.day:
        now = datetime.datetime.now()
        instance.day = now.strftime("%A")

    if instance.profit_n_loss and instance.charges:
        instance.net_profit_n_loss = instance.profit_n_loss - instance.charges
    else:
        instance.net_profit_n_loss = instance.profit_n_loss

    if instance.tradingdaytrade_set.all().count() > 0:
        instance.profit_n_loss = 0
        for trade in instance.tradingdaytrade_set.all():
            instance.profit_n_loss = instance.profit_n_loss + trade.profit_n_loss
        if instance.profit_n_loss < 0:
            instance.is_profit = False

    if instance.amount_used:
        instance.pnl_percentage = (instance.net_profit_n_loss/instance.amount_used)*100


def trading_day_trade_receiver(sender, instance, *args, **kwargs):
    instance.profit_n_loss = instance.quantity*(instance.sell_price-instance.buy_price)

    if instance.profit_n_loss < 0:
        instance.is_profit = False

    


pre_save.connect(trading_day_receiver, sender=TradingDay)
pre_save.connect(trading_day_trade_receiver, sender=TradingDayTrade)