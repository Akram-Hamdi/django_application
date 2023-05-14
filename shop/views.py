
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import FournisseurForm, ProduitForm
from shop.models import Fournisseur, Produit
from .serializers import ProduitSerializer, FournisseurSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categorie
from .serializers import CategorieSerializer

class CategorieAPIView(APIView):
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)

class FournisseurAPIView(APIView):
    def get(self, request):
        fournisseurs = Fournisseur.objects.all()
        serializer = FournisseurSerializer(fournisseurs, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    
# Create your views here.

# def my_view(request):
#     request.session['username'] = 'john'

# def my_other_view(request):
#     username = request.session.get('username', None)    


def home(request):
    return render(request, 'shop/home.html')

def fournisseur(request):
   fournisseur=Fournisseur.objects.all()
   return render(request, 'shop/fournisseur.html',{'fournisseur':fournisseur})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject=request.POST['subject']
        message = request.POST['message']
        message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['akramhamdi299@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'shop/contact.html', {'success': True})
    return render(request, 'shop/contact.html')

#----------------------------------------- CRUD Produit ------------------------------------------
def produit(request):
    produits=Produit.objects.all()
    return render(request,'shop/produit.html',{'produits':produits})

# def ajouter_au_panier(request):
#     produit_id = request.POST.get('produit_id')
#     produit = get_object_or_404(Produit, id=produit_id)

#     cart = request.session.get('cart', {})

#     if produit_id in cart:
#         cart[produit_id]['quantite'] += 1
#     else:
#         cart[produit_id] = {
#             'nom': produit.libelle,
#             'quantite': 1,
#             'prix': produit.prix,
#         }

#     request.session['cart'] = cart

#     return redirect('panier')
def panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0

    for produit_id, produit_data in panier.items():
        produit = get_object_or_404(Produit, pk=produit_id)
        quantite = produit_data['quantite']
        prix_total = produit.prix * quantite
        total += prix_total
        produits.append({
            'produit': produit,
            'quantite': quantite,
            'prix_total': prix_total
        })

    return render(request, 'shop/panier.html', {'produits': produits, 'total': total})

def ajouter_au_panier(request, produit_id):
    panier = request.session.get('panier', {})
    produit = get_object_or_404(Produit, pk=produit_id)
    quantite = int(request.POST.get('quantite', 1))

    if produit_id in panier:
        panier[produit_id]['quantite'] += quantite
    else:
        panier[produit_id] = {'quantite': quantite}

    request.session['panier'] = panier
    messages.success(request, "Le produit a été ajouté au panier.")
    return redirect('produit')

def supprimer_produit(request, produit_id):
    panier = request.session.get('panier', {})
    produit = get_object_or_404(Produit, pk=produit_id)

    if produit_id in panier:
        del panier[produit_id]
        request.session['panier'] = panier

    return redirect('panier')

def vider_panier(request):
    request.session['panier'] = {}
    messages.success(request, "Le panier a été vidé.")
    return redirect('panier')

#----------------------------------------- ADD Produit ------------------------------------------

def add_produit(request):
    form = ProduitForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('produit')
    return render(request, 'shop/ajouter_produit.html', {'form': form})

#----------------------------------------- EDIT Produit ------------------------------------------

def edit_produit(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    form = ProduitForm(request.POST or None, request.FILES or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('produit')
    return render(request, 'shop/modifier_produit.html', {'form': form})

#----------------------------------------- DELETE Produit ------------------------------------------

def delete_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return redirect('produit')

def filter_by_category(request, category):
    produits = Produit.objects.filter(categorie__name=category)
    context = {'produits': produits}
    return render(request, 'shop/produit.html', context)


#-------------------------------------x----END CRUD Produit----x--------------------------------------

#----------------------------------------- ADD FOURNISSEUR ------------------------------------------

def add_fournisseur(request):
    form = FournisseurForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('fournisseur')
    return render(request, 'shop/ajouter_fournisseur.html', {'form': form})

#----------------------------------------- EDIT FOURNISSEUR ------------------------------------------

def edit_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    form = FournisseurForm(request.POST or None, request.FILES or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('fournisseur')
    return render(request, 'shop/modifier_fournisseur.html', {'form': form})

#----------------------------------------- DELETE FOURNISSEUR ------------------------------------------

def delete_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, id=
    fournisseur_id)
    fournisseur.delete()
    return redirect('fournisseur')

#-------------------------------------x----END CRUD FOURNISSEUR----x--------------------------------------


