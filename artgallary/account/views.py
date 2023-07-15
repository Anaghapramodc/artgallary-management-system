from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.



class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('art-list')  # Update the next_page attribute

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('art-list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')


