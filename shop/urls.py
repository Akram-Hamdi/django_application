from django.urls import path
from . import views
from .views import CategorieAPIView,FournisseurAPIView,ProduitAPIView

urlpatterns=[
    path('api/category/', CategorieAPIView.as_view(), name='categories'),
    path('api/fournisseur/', FournisseurAPIView.as_view(), name='fournisseurs'),
    path('api/produit/', ProduitAPIView.as_view(), name='produits'),
    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.panier, name='panier'),
    path('panier/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),

    path('vider-panier/', views.vider_panier, name='vider_panier'),
    path('produit/', views.produit, name='produit'),
    path('produit/ajouter/', views.add_produit, name='ajouter_produit'),
    path('produit/modifier/<int:produit_id>/', views.edit_produit, name='modifier_produit'),
    path('produit/<int:produit_id>/delete/', views.delete_produit, name='delete_produit'),
    path('produits/<str:category>/', views.filter_by_category, name='filter_by_category'),

    
    path('fournisseur/', views.fournisseur, name='fournisseur'),
    path('fournisseur/ajouter/', views.add_fournisseur, name='ajouter_fournisseur'),
    path('fournisseur/modifier/<int:fournisseur_id>/', views.edit_fournisseur, name='modifier_fournisseur'),
    path('fournisseur/<int:fournisseur_id>/delete/', views.delete_fournisseur, name='delete_fournisseur'),

    path('contact/',views.contact, name='contact'),
    path('', views.home, name='home'),
]
