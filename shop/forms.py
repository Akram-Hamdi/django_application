from django.forms import ModelForm
from .models import Produit
from .models import Fournisseur
from .models import Commande, Produit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = ['dateCde', 'totalCde', 'produits']

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'email', 'telephone']
        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ('libelle', 'description', 'prix', 'type', 'img', 'categorie', 'fournisseur')

