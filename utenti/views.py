from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'utenti/login.html'
    def get_success_url(self):
        return reverse_lazy('home_eventi')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home_eventi')