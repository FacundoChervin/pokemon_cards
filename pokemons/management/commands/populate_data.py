from typing import Collection
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from pokemons.models import Rarity, Type, Card, Expansion
import requests
from scrapper.load_cards import get_cards
from django.db.utils import IntegrityError

url_types = "https://api.pokemontcg.io/v2/types"

def load_constants():
    types_response = requests.get(url_types).json()["data"]
    rarities = ["Common", "Uncommon", "Rare"]
    expansions = ["Base Set", "Jungle","Fossil",
                  "Base Set 2","Team Rocket","Gym Heroes",
                  "Gym Challenge","Neo Genesis","Neo Discovery",
                  "Neo Revelation","Neo Destiny","Legendary",
                  "Collection","Expedition Base","Set","Aquapolis",
                  "Skyridge","EX Ruby & Sapphire","EX Sandstorm",
                  "EX Dragon","EX Team Magma vs Team Aqua","EX Hidden",
                  "Legends","EX FireRed & LeafGreen","EX Team Rocket Returns",
                  "EX Deoxys","EX Emerald","EX Unseen Forces","EX Delta Species",
                  "EX Legend Maker","Phantoms","EX Holon","EX Crystal Guardians", 
                  "EX Dragon Frontiers", "EX Power Keepers", "Diamond & Pearl", 
                  "Mysterious Treasures", "Secret Wonders", "Great Encounters",
                  "Majestic Dawn","Legends Awakened","Stormfront","Platinum",
                  "Rising Rivals","Supreme Victors","Arceus","HeartGold & SoulSilver",
                  "Unleashed","Undaunted","Triumphant","Call of Legends","Black & White",
                  "Emerging Powers","Noble Victories","Next Destinies","Dark Explorers",
                  "Dragons Exalted","Boundaries Crossed","Plasma Freeze","Plasma Storm",
                  "Plasma Blast","Legendary Treasures","XY","Flashfire","Furious Fists",
                  "Phantom Forces","Primal Clash","Roaring Skies","Ancient Origins",
                  "BREAKthrough","BREAKpoint","Fates Collide","Steam Siege","Evolutions",
                  "Sun & Moon","Guardians Rising","Burning Shadows","Crimson Invasion",
                  "Ultra Prism","Forbidden Light","Celestial Storm","Lost Thunder",
                  "Team Up","Unbroken Bonds", "Unified Minds", "Cosmic Eclipse", 
                  "Sword & Shield", "Rebel Clash", "Darkness Ablaze", "Vivid Voltage", 
                  "Battle Styles","Chilling Reign","Evolving Skies"]
    
    for expansion in expansions:
        expansion_obj = Expansion(expansion_desc=expansion)
        expansion_obj.save()
    
    for rarity in rarities:
        rarity_obj = Rarity(rarity_desc=rarity)
        rarity_obj.save()
        
    for type in types_response:
        type_obj = Type(type_desc=type)
        type_obj.save()

def load_cards():
    cards_dict = get_cards()

    for card in cards_dict:
        pokemon_name = card["pokemon_name"]
        pokemon_hp = card["pokemon_hp"]
        is_first_edition = card["is_first_edition"]
        expansion = card["expansion"]
        type = card["type"]
        rarity = card["rarity"]
        price = card["price"]
        image = card["image"]
        creation_date = card["creation_date"]      
        creation_date = creation_date.replace("/","-")
        rarity_obj = Rarity.objects.get(rarity_desc=rarity)
        
        card_obj = Card(card_name=pokemon_name,
                        card_hp=pokemon_hp,
                        card_is_first_edition=is_first_edition,
                        card_expansion=expansion,
                        card_rarity=rarity_obj,
                        card_type=type,
                        card_price=price,
                        card_image=image,
                        card_creation_date=creation_date,)
        try:
            card_obj.save()
        except IntegrityError as err:
            print("Ignoring unhandled integrity error:")
            print(err)
        print("{} saved".format(pokemon_name))
        
       
                    

class Command(BaseCommand):
    help = 'Populate data to the DB'
    
    def handle(self, *args, **kwargs):
        # load_constants()
        load_cards()

    

        
## AGREGAR EXCEPCIONES POR REPETIDOS 