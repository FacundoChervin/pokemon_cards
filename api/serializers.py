from rest_framework import serializers
from pokemons.models import Card, Type, Rarity, Expansion

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("type_desc",)

class RaritySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ("rarity_desc",)
        
        
class ExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expansion
        fields = ("expansion_desc",)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_id_tcg", 
                  "card_name", 
                  "card_hp", 
                  "card_is_first_edition", 
                  "card_expansion", 
                  "card_type", 
                  "card_rarity", 
                  "card_price", 
                  "card_image", 
                  "card_creation_date")
