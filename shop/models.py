from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

TYPE_CHOICES=[
    ('em','emballé'),
    ('fr','Frais'),
    ('cs','Conserve')
]

class Produit(models.Model):
    id = models.AutoField(primary_key=True)    
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.libelle 

class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    cree = models.DateTimeField(auto_now_add=True)
    modifie = models.DateTimeField(auto_now=True)


class Categorie(models.Model):
    TYPE_CHOICES=[('AL','Alimentaire'),
                  ('Lg','Linge de Maison'),
                  ('El','Electronique'),
                  ('DC','Design-Creation')
    ]
    name=models.CharField(max_length=50,default='Al',choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(null=True)
    email=models.EmailField()
    telephone=models.CharField(max_length=8)

    def __str__(self):
        return (self.nom+','+self.adresse+','+self.email+','+self.telephone)    

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    
    def __str__(self):
        return "objet ProduitNC:%s"%(self.Duree_garantie)
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField('Produit')

    def __str__(self):
        return str(self.dateCde) + ' - ' + str(self.totalCde)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.produit.libelle} ({self.user.username})"
