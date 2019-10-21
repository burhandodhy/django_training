from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, ProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
      
      #password validation
      if password1 ==  password2:

        # check username.
        if User.objects.filter(username=username).exists():
          messages.warning(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():   
          messages.warning(request, 'Email already exists')
        else:
          User.objects.create_user(username = username, email=email, password= password1, first_name=first_name, last_name=last_name)
          messages.success(request, 'User Regisration Successfully. Please login.')
          return HttpResponseRedirect('login')

      else:
        messages.warning(request,'Password do not match.')

  else:
    form = RegisterForm()


  context = {
      'form': form
  }
  return render(request, 'authenticate/register.html', context)


def login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = auth.authenticate(username=username, password=password)  

      if user is not None:
        auth.login(request, user)
        messages.success(request,'Login Successfully Login.')
        return redirect('home')
      else:
        messages.warning(request,'Invalid username or password.')

  else:
    form = LoginForm()

  context = {
      'form': form
  }
  return render(request, 'authenticate/login.html',context)

# Only loggedin user access the profile page.
@login_required(login_url='/login')
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
        messages.warning(request,'Password do not match.')
        return HttpResponseRedirect('profile')
          

      if user.email != email and User.objects.filter(email=email).exists():   
        messages.warning(request, 'Email already exists')
      else:
        user.first_name = first_name;
        user.last_name = last_name;
        user.email = email;

        if password1 != '' or password2 != '':
          user.set_password(password1)
          # django logout the user when password is change. We update the session auth to keep the user loggedin.
          auth.update_session_auth_hash(request,user)
        
        user.save();
        messages.success(request,'Profile Updated.')
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
    messages.success(request,'Successfully logout!')
  return redirect('home')
