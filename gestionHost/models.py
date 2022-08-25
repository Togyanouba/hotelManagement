from tkinter import CASCADE
from django.db import models
from django.conf import Settings




class Client(models.Model):
    qualitePersonne= (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),
        ('Mlle', 'Mademoiselle'),
        ('Autres', 'Autres'),
    )
    qualite= models.CharField(max_length=6, choices=qualitePersonne)
    nom=models.CharField(max_length=15)
    prenom= models.CharField(max_length=25)
    adresse= models.CharField(max_length=25)
    telephone =models.IntegerField(default=0)
    email= models.EmailField(max_length=45)
    
    def __str__(self):
        return f'{self.qualite }  {self.nom } {self.prenom} : {self.adresse}'
    
#creation des models pour la reservation de chambre
class Chambre(models.Model):
    categoriesChambres= (
        ('Chambre simple' ,'Chambre Simple'),
        ('Chambre double', 'Chambre Double'),
        ('Chambre de luxe', 'Chambre de Luxe'),
        ('Appartement', 'Appartement'),
        
    )
    numero=models.IntegerField(unique=True);
    categorie= models.CharField(max_length=15, choices=categoriesChambres)
    description= models.TextField()
    prix = models.IntegerField()
    image =models.ImageField(upload_to='media/imageUser')
    disponibilite=models.BooleanField(default=True);
    
    def __str__(self):
        return f'{self.numero}, {self.categorie }'
    
class Reservation(models.Model):
    utilisateur= models.ForeignKey(Client, on_delete= models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete= models.CASCADE)
    dateEntre= models.DateTimeField()
    dateSorti= models.DateTimeField()
    
    def __str__(self):
        return f'{self.utilisateur} a reservé la chambre {self.chambre} à partir de {self.dateEntre} au {self.dateSorti} '

#creation des models pour l'achat et la reservation des plats

class MenuArticles(models.Model):
    nom= models.CharField(max_length=100),
    prix=models.DecimalField(max_digits=5, decimal_places=3),
    description=models.TextField(),
    image= models.ImageField(upload_to='media/imagePlat'),
    categorie= models.ManyToManyField('Categorie', related_name='articles'),
    
    def __str__(self):
        return self.nom
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom 

#creation des models pour la facture

class Facture(models.Model):
    numFacture=models.IntegerField(),
    typePayement=models.TextField(max_length=15),
    client= models.ForeignKey(Client, on_delete= models.CASCADE),
    
    def __str__(self):
        return self.numFacture