from django.contrib import admin
from .models import Chambre, Facture, Reservation, Client, Categorie, MenuArticles

# Register your models here.
admin.site.register(Chambre)
admin.site.register(Reservation)
admin.site.register(Client)
admin.site.register(Categorie)
admin.site.register(MenuArticles)
admin.site.register(Facture)

