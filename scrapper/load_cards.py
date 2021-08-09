import random
import requests


url = "https://api.pokemontcg.io/v2/cards/"

min = 1
max = 2

## TESTEAR CON MAS MAXIMOS

cards_dict = []
def get_cards():
    for i in range(min, max):
        cards = requests.get(url+"?page={}".format(i)).json()
        cards_data = cards["data"]

        for card in cards_data:
    
            save = True
            pokemon_name = card["name"]
            has_first_edition = True if "1stEditionHolofoil" in card["tcgplayer"]["prices"] else False

            pokemon_hp = card["hp"]
            
            is_first_edition = bool(random.getrandbits(1)) if has_first_edition else False
            expansion = card["set"]["name"]
            type = card["types"][0]

            if "rarity" in card:
                rarity = card["rarity"]
                save = True
                
            else:
                save = False
                    
            rarity_to_save = "Common"
            if rarity == "Common":
                rarity_to_save = "Common"
            elif rarity == "Uncommon":
                rarity_to_save = "Uncommon"
            elif "rare" in rarity:
                rarity_to_save = "Rare"    
                
            prices = card["tcgplayer"]["prices"]
            if "normal" in prices:
                normal_price = card["tcgplayer"]["prices"]["normal"]["mid"]
            elif "holofoil" in prices:
                normal_price = card["tcgplayer"]["prices"]["holofoil"]["mid"]
            elif "reverseHolofoil" in prices:
                normal_price = card["tcgplayer"]["prices"]["reverseHolofoil"]["mid"]
            price = card["tcgplayer"]["prices"]["1stEditionHolofoil"]["mid"] if is_first_edition else normal_price
            image = card["images"]["small"]
            creation_date = card["set"]["releaseDate"]
            if(save):
                card_object = {
                    "pokemon_name": pokemon_name,
                    "pokemon_hp": pokemon_hp,
                    "is_first_edition": is_first_edition,
                    "expansion": expansion,
                    "type": type,
                    "rarity": rarity_to_save,
                    "price": price,
                    "image": image,
                    "creation_date": creation_date 
                }
                cards_dict.append(card_object)
    return cards_dict   