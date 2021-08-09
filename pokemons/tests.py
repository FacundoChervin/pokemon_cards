from django.test import TestCase

from pokemons.models import Card


class CardTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_card_1 = Card.objects.create(
                        card_name= "test1",
                        card_hp= 100,
                        card_is_first_edition= True,
                        card_expansion= 'Secret Wonders',
                        card_type= 'Colorless',
                        card_rarity= 'Common',
                        card_price= 2,
                        card_image= 'https://images.pokemontcg.io/gym2/1.png',
                        card_creation_date= "2000-08-14")
        test_card_1.save()
        
    def test_card(self):
        card = Card.objects.get(id=1)
        expected_card_name = f'{card.card_name}'
        expected_card_hp = f'{card.card_hp}'
        expected_card_is_first_edition = f'{card.card_is_first_edition}'
        expected_card_expansion = f'{card.card_expansion}'
        expected_card_type = f'{card.card_type}'
        expected_card_rarity = f'{card.card_rarity}'
        expected_card_price = f'{card.card_price}'
        expected_card_image = f'{card.card_image}'
        expected_card_creation_date = f'{card.card_creation_date}'

        self.assertEquals(expected_card_name, 'test1')
        self.assertEquals(expected_card_hp,100)
        self.assertEquals(expected_card_is_first_edition,True)
        self.assertEquals(expected_card_expansion,'Secret Wonders')
        self.assertEquals(expected_card_type,"Colorless")
        self.assertEquals(expected_card_rarity,'Common')
        self.assertEquals(expected_card_price,2)
        self.assertEquals(expected_card_image,'https://images.pokemontcg.io/gym2/1.png')
        self.assertEquals(expected_card_creation_date,"2000-08-14")
        
        
