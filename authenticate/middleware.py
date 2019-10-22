from django.shortcuts import redirect
from django.contrib import auth, messages
from django.utils.translation import gettext as _


class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        path_info = request.path_info

        if path_info == '/profile' and not request.user.is_authenticated:
            return redirect('/login')

        if path_info == '/login' and request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, _('Login Successfully Login.'))
                return redirect('home')
            else:
                messages.warning(request, _('Invalid username or password.'))

