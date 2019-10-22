from django import forms


class RegisterForm(forms.Form):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50, required=True)
  username = forms.CharField(max_length=50, required=True)
  email = forms.EmailField(required=True)
  date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1980, 2020)))
  country = forms.CharField(max_length=50, required=True)
  state = forms.CharField(max_length=50, required=True)
  password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
  password2 = forms.CharField(widget=forms.PasswordInput(), required=True)


class LoginForm(forms.Form):
  username = forms.CharField(max_length=50, required=True)
  password = forms.CharField(widget=forms.PasswordInput(), required=True)


class ProfileForm(forms.Form):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50, required=True)
  email = forms.EmailField(required=True)
  password1 = forms.CharField(widget=forms.PasswordInput(), required=False)
  password2 = forms.CharField(widget=forms.PasswordInput(), required=False)
