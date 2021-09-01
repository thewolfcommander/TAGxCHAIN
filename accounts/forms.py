from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Form for handling logging in
    """
    username = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = [
            'username',
        ]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-12 mb-4'),
                Column('password', css_class='form-group col-md-12 mb-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Login')
        )

    
class NewUserForm(UserCreationForm):
    """
    Form for new user registration
    """
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, label="First name", widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(required=True, label="Last name", widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-6'),
                Column('last_name', css_class='form-group col-md-6 mb-6'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-6'),
                Column('username', css_class='form-group col-md-6 mb-6'),
                Column('password1', css_class='form-group col-md-6 mb-6'),
                Column('password2', css_class='form-group col-md-6 mb-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Register')
        )

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

    

class EditUserForm(forms.ModelForm):
    """
    Form for edit user details
    """
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, label="First name", widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(required=True, label="Last name", widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-6'),
                Column('last_name', css_class='form-group col-md-6 mb-6'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-6'),
                Column('username', css_class='form-group col-md-6 mb-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )