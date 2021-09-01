from django.db import models

# Create your models here.

class Country(models.Model):
    """
    Model for handling country data for tagxchain platform
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Exchange(models.Model):
    """
    Model for handling exchange data for tagxchain platform
    """
    DATA_TYPE = [
        ('delayed_stocks', 'Delayed Stocks'),
        ('delayed_futures', 'Delayed Futures'),
        ('delayed_stocks_n_indexes', 'Delayed Stocks & Indexes'),
        ('delayed_stocks_indexes_n_futures', 'Delayed Stocks, Indexes & Futures'),
        ('real_time_stocks','Real-time Stocks'),
        ('real_time_futures', 'Real-time Futures'),
        ('real_time_stocks_n_indexes', 'Real-time Stocks & Indexes'),
        ('real_time_indexes', 'Real-time Indexes'),
        ('real_time_forex', 'Real-time Forex'),
        ('real_time_cryptocurrencies', 'Real-time Cryptocurrencies'),
        ('eod_stocks', 'EOD Stocks'),
        ('eod_futures', 'EOD Futures'),
        ('eod_stocks_n_certificates', 'EOD Stocks & Certificates'),
        ('eod_stocks_n_indexes', 'EOD Stocks & Indexes'),
        ('eod_stocks_futures_n_indexes', 'EOD Stocks, Indexes & Futures'),
    ]
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    data_provider = models.CharField(max_length=255, null=True, blank=True)
    data_type = models.CharField(max_length=255, null=True, blank=True, choices=DATA_TYPE, default='delayed_stocks')
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Scripts(models.Model):
    """
    Model for handling the scripts for tagxchain platform
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    symbol = models.CharField(max_length=255, null=True, blank=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name