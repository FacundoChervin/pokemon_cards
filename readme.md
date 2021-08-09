# 1.	The card object
## Attributes

#### Id *integer*
Unique identifier for the card.

### *card_name string*

The name of the card.

### card_hp *integer*

The hit points of the card.
Constraint: Must be a multiple of 10.

### card_is_first_edition *boolean*

Defines if the card is first edition.
Possible values: true, false.

### card_expansion *string*

Expansion set of the card.
Possible values: Base Set, Jungle, Fossil, Base Set 2, Team Rocket, Gym Heroes, Gym Challenge, Neo Genesis, Neo Discovery, Neo Revelation, Neo Destiny, Legendary, Collection, Expedition Base, Set, Aquapolis, Skyridge, EX Ruby & Sapphire, EX Sandstorm, EX Dragon, EX Team Magma vs Team Aqua, EX Hidden, Legends, EX FireRed & LeafGreen, EX Team Rocket Returns, EX Deoxys, EX Emerald, EX Unseen Forces, EX Delta Species, EX Legend Maker, Phantoms, EX Holon, EX Crystal Guardians, EX Dragon Frontiers, EX Power Keepers, Diamond & Pearl, Mysterious Treasures, Secret Wonders, Great Encounters, Majestic Dawn, Legends Awakened, Stormfront, Platinum, Rising Rivals, Supreme Victors, Arceus, HeartGold & SoulSilver, Unleashed, Undaunted, Triumphant, Call of Legends, Black & White, Emerging Powers, Noble Victories, Next Destinies, Dark Explorers, Dragons Exalted, Boundaries Crossed, Plasma Freeze, Plasma Storm, Plasma Blast, Legendary Treasures, XY, Flashfire, Furious Fists, Phantom Forces, Primal Clash, Roaring Skies, Ancient Origins, BREAKthrough, BREAKpoint, Fates Collide, Steam Siege, Evolutions, Sun & Moon, Guardians Rising, Burning Shadows, Crimson Invasion, Ultra Prism, Forbidden Light, Celestial Storm, Lost Thunder, Team Up, Unbroken Bonds, Unified Minds, Cosmic Eclipse, Sword & Shield, Rebel Clash, Darkness Ablaze, Vivid Voltage, Battle Styles, Chilling Reign, Evolving Skies.
	
### card_type *string*

Type of the card.
Possible values: Colorless, Darkness, Dragon, Fairy, Fighting, Fire, Grass, Lightning, Metal, Psychic, Water.

### card_rarity *string*

Rarity of the card.
Possible values: Common, Uncommon, Rare.

### card_price *Float*

Average price of the card.

### card_image string

Link to the image of the card.
Must finish in .png or .jpg.
	
### card_creation_date *date*

Creation date of the card.
Format: YYYY-MM-DD

# 2.	Get all cards

##### URL: http://localhost:8000/pokemon-cards/api/v1/cards/
##### METHOD: GET
##### Example: GET http://localhost:8000/pokemon-cards/api/v1/cards/

![image](https://user-images.githubusercontent.com/26860405/128710302-23fe2439-4400-4a30-8b80-da7104e5ddbc.png)

# 3.	Get single card

##### URL: http://localhost:8000/pokemon-cards/api/v1/cards/{Key}
##### Method: GET
##### Parameter: KEY *integer*
##### Example: GET http://localhost:8000/pokemon-cards/api/v1/cards/3

![image](https://user-images.githubusercontent.com/26860405/128710375-3edbd475-bc03-4893-8e61-72f94e22f5d2.png)

# 4.	Delete a card

##### URL: http://localhost:8000/pokemon-cards/api/v1/cards/{Key}
##### Method: DELETE
##### Parameter: Key *integer*

# 5.	Update a card

##### URL: http://localhost:8000/pokemon-cards/api/v1/cards/{Key}
##### Method: PUT
##### Parameter: Key *integer*

![image](https://user-images.githubusercontent.com/26860405/128710549-d4c32b61-3664-49e9-a653-742beac4adb7.png)

##### Example: 

![image](https://user-images.githubusercontent.com/26860405/128710611-413e0fb5-076b-4b34-9ace-e10fcedadab8.png)

# 6.	Create a card

##### URL: http://localhost:8000/pokemon-cards/api/v1/cards/create
##### METHOD: POST
##### Body: 

![image](https://user-images.githubusercontent.com/26860405/128710675-e7340aa4-890a-49c0-ae53-84f356fe99a1.png)

##### Example:

![image](https://user-images.githubusercontent.com/26860405/128710733-f9e8c8b5-fbce-4efb-8a3a-c58c63111ace.png)

# 7.	Filtering

You can filter the Get all cards with URL parameters.
Possible Filters:

![image](https://user-images.githubusercontent.com/26860405/128710805-11da4039-1ba3-401d-928f-e8a1976613d0.png)

##### Possible Search fields:
###### card_name
###### card_expansion
###### card_type
###### card_rarity


##### Possible Ordering fields:
###### card_name
###### card_price
###### card_creation_date
###### id
###### card_hp
  
Examples:
http://localhost:8000/pokemon-cards/api/v1/cards/?card_name=Caterpie
http://localhost:8000/pokemon-cards/api/v1/cards/?card_hp__gte=50&ordering=card_hp

# 8.	Pagination

You can restrict the amount of cards per page you would get.
##### Parameters:
###### page_size: Defines the amount of cards per page
###### 	page: Define the page Number to get.

Examples:
http://localhost:8000/pokemon-cards/api/v1/cards/?page_size=2
http://localhost:8000/pokemon-cards/api/v1/cards/?page_size=2&page=5
