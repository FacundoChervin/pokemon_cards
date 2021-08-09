from django.db import models

# Create your models here.

class Type(models.Model):
    type_desc = models.CharField(max_length=250, unique=True)
    
    class Meta:
        ordering = ['type_desc']

    def __str__(self):
        return self.type_desc
    
class Rarity(models.Model):
    rarity_desc = models.CharField(max_length=250, unique=True)
    
    class Meta:
        ordering = ['rarity_desc']

    def __str__(self):
        return self.rarity_desc

class Expansion(models.Model):
    expansion_desc = models.CharField(max_length=250)
    
    class Meta:
        ordering = ['expansion_desc']
        
    def __str__(self):
        return self.expansion_desc

class Card(models.Model):
    card_id_tcg = models.CharField(max_length=100, null=True, default="NO_TCG")
    card_name = models.CharField(max_length=250)
    card_hp = models.IntegerField()
    card_is_first_edition = models.BooleanField()
    card_expansion = models.CharField(max_length=250)
    card_type = models.CharField(max_length=250)
    card_rarity = models.CharField(max_length=250)
    card_price = models.FloatField()
    card_image = models.CharField(max_length=250, default="https://http2.mlstatic.com/D_NQ_NP_681808-MLA44856858037_022021-O.jpg")
    card_creation_date = models.DateField()
    
    class Meta:
        ordering = ['card_name']

    def __str__(self):
        return self.card_name
    
