from rest_framework import serializers
from .models import Produit, Categorie, Fournisseur, Commande

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = ['id', 'nom','adresse','email']

class ProduitSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()
    fournisseur = FournisseurSerializer()

    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'prix', 'fournisseur','categorie']

class CommandeSerializer(serializers.ModelSerializer):
    produits = ProduitSerializer(many=True)

    class Meta:
        model = Commande
        fields = '_all_'