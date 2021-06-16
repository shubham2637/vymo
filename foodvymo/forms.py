from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Merchant


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12, min_length=10, required=True, label=_('Phone Number'),
                                 widget=(forms.TextInput(attrs={'class': 'form-control'})))

    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                )
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )

    class Meta:
        model = User
        fields = ('first_name','last_name','phone_number' ,'username', 'password1', 'password2',)




