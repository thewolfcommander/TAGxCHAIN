from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from trades.models import TradingDay


class TradingDayForm(forms.ModelForm):
    """
    Form for edit user details
    """
    charges = forms.DecimalField(required=False, label="Broking Charges", widget=forms.NumberInput(attrs={'placeholder': 'Enter Broking Charges'}))
    remarks = forms.CharField(required=False, label="Remarks", widget=forms.Textarea(attrs={'placeholder': "Want to add some special comments?"}))

    class Meta:
        model = TradingDay
        fields = [
            'user',
            'date',
            'charges',
            'remarks',
            'profit_n_loss',
            'amount_used',
            'is_front',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('date', css_class='form-group col-md-6 mb-6'),
                Column('charges', css_class='form-group col-md-6 mb-6'),
                css_class='form-row'
            ),
            Row(
                Column('remarks', css_class='form-group col-md-12 mb-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )


class TradingDayTradeForm(forms.ModelForm):
    """
    Form for edit trading day trade details
    """
    POSITION_CHOICES = [
        ('Short', 'Short'),
        ('Long', 'Long')
    ]
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=False, label="Position of Trade")
    symbol = forms.CharField(required=False, label="Symbol", widget=forms.TextInput(attrs={'placeholder': "Symbol of Instrument"}))
    quantity = forms.IntegerField(required=False, label="Quantity", widget=forms.NumberInput(attrs={'placeholder': "How much you've traded?"}))
    buy_price = forms.DecimalField(required=False, label="Buy Price", widget=forms.NumberInput(attrs={'placeholder': 'Enter Buy Price'}))
    sell_price = forms.DecimalField(required=False, label="Sell Price", widget=forms.NumberInput(attrs={'placeholder': 'Enter Sell Price'}))
    expected_target = forms.DecimalField(required=False, label="Expected Target Price", widget=forms.NumberInput(attrs={'placeholder': 'Enter Expected Target Price'}))
    stop_loss = forms.DecimalField(required=False, label="Stop Loss", widget=forms.NumberInput(attrs={'placeholder': 'Enter Stop Loss'}))
    
    remarks = forms.CharField(required=False, label="Remarks", widget=forms.Textarea(attrs={'placeholder': "Want to add some special comments?"}))

    class Meta:
        model = TradingDay
        fields = [
            'position',
            'symbol',
            'quantity',
            'buy_price',
            'sell_price',
            'expected_target',
            'stop_loss',
            'remarks',
            'profit_n_loss'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('position', css_class='form-group col-md-3 mb-6'),
                Column('symbol', css_class='form-group col-md-3 mb-6'),
                Column('quantity', css_class='form-group col-md-3 mb-6'),
                css_class='form-row'
            ),
            Row(
                Column('buy_price', css_class='form-group col-md-3 mb-6'),
                Column('sell_price', css_class='form-group col-md-3 mb-6'),
                Column('expected_target', css_class='form-group col-md-3 mb-6'),
                Column('stop_loss', css_class='form-group col-md-3 mb-6'),
                css_class='form-row'
            ),
            Row(
                Column('remarks', css_class='form-group col-md-12 mb-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )