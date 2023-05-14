from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from shop.forms import UserRegistrationForm

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # enregistre l'utilisateur dans la base de données
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html' # template pour afficher le formulaire de connexion
    redirect_authenticated_user = True # redirection automatique si l'utilisateur est déjà connecté
    extra_context = {'page_title': 'Login'} # informations supplémentaires à passer au template

    def get_success_url(self):
        # redirection après une connexion réussie
        return reverse_lazy('home')