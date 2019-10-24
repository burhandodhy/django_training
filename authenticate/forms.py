from django import forms
from django.utils.translation import gettext as _

class RegisterForm(forms.Form):
  first_name = forms.CharField(label=_('First Name'),max_length=50, required=True)
  last_name = forms.CharField(label=_('Last Name'),max_length=50, required=True)
  username = forms.CharField(label=_('Username'),max_length=50, required=True)
  email = forms.EmailField(label=_('Email'),required=True)
  date_of_birth = forms.DateField(label=_('Date of birth'),required=True, widget=forms.SelectDateWidget(years=range(1980, 2020)))
  country = forms.CharField(label=_('Country'),max_length=50, required=True)
  state = forms.CharField(label=_('State'),max_length=50, required=True)
  password1 = forms.CharField(label=_('Password'),widget=forms.PasswordInput(), required=True)
  password2 = forms.CharField(label=_('Repeat Password'),widget=forms.PasswordInput(), required=True)


class LoginForm(forms.Form):
  username = forms.CharField(label=_('Username'),max_length=50, required=True)
  password = forms.CharField(label=_('Password'),widget=forms.PasswordInput(), required=True)


class ProfileForm(forms.Form):
  first_name = forms.CharField(label=_('First Name'),max_length=50, required=True)
  last_name = forms.CharField(label=_('Last Name'),max_length=50, required=True)
  email = forms.EmailField(label=_('Email'),required=True)
  password1 = forms.CharField(label=_('Password'),widget=forms.PasswordInput(), required=False)
  password2 = forms.CharField(label=_('Repeat Password'),widget=forms.PasswordInput(), required=False)
