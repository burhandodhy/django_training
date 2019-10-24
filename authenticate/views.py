from django.shortcuts import render,redirect
from django.contrib import messages, auth
from authenticate.models import CustomUser
from authenticate.forms import RegisterForm, LoginForm, ProfileForm
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

def home(request):
  return render(request,'authenticate/home.html')

def register(request):
  
  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      # Get form values
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      username = form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      password1 = form.cleaned_data.get('password1')
      password2 = form.cleaned_data.get('password2')
      date_of_birth = form.cleaned_data.get('date_of_birth')
      country = form.cleaned_data.get('country')
      state = form.cleaned_data.get('state')
      
      #password validation
      if password1 ==  password2:

        # check username.
        if CustomUser.objects.filter(username=username).exists():
          messages.warning(request, 'Username already exists')
        elif CustomUser.objects.filter(email=email).exists():   
          messages.warning(request, _('Email already exists'))
        else:
          CustomUser.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name,state=state, date_of_birth=date_of_birth,country=country)
          messages.success(request, _('User Regisration Successfully. Please login.'))
          return HttpResponseRedirect('login')

      else:
        messages.warning(request,_('Password do not match.'))

  else:
    form = RegisterForm()


  context = {
      'form': form
  }
  return render(request, 'authenticate/register.html', context)


def login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)
  else:
    form = LoginForm()

  context = {
      'form': form
  }
  return render(request, 'authenticate/login.html',context)


def profile(request):

  if request.method == 'POST':
    form = ProfileForm(request.POST)

    if form.is_valid():
      # Get form values
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      email = form.cleaned_data.get('email')
      password1 = form.cleaned_data.get('password1')
      password2 = form.cleaned_data.get('password2')
      user = request.user;

      # Password change 
      if ( password1 != '' or password2 != '' ) and ( password1 !=  password2 ):
        messages.warning(request, _('Password do not match.'))
        return HttpResponseRedirect('profile')
          

      if user.email != email and CustomUser.objects.filter(email=email).exists():   
        messages.warning(request, _('Email already exists'))
      else:
        user.first_name = first_name;
        user.last_name = last_name;
        user.email = email;

        if password1 != '' or password2 != '':
          user.set_password(password1)
          # django logout the user when password is change. We update the session auth to keep the user loggedin.
          auth.update_session_auth_hash(request,user)
        
        user.save();
        messages.success(request, _('Profile Updated.'))
        return HttpResponseRedirect('profile')


  context = {
    'form': ProfileForm({
      'first_name' : request.user.first_name,
      'last_name' : request.user.last_name,
      'email' : request.user.email
    })
  }
  return render(request,'authenticate/profile.html', context)


def logout(request):
  if request.user.is_authenticated:
    auth.logout(request)
    messages.success(request, _('Successfully logout!'))
  return redirect('home')
