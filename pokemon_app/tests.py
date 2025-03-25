from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Pokemon

# Create your tests here.
class pokemon_test(TestCase):
    
    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name = 'Lucario', description = 'The best pokemon.')
        try:
             # remember validators are not ran on our new instance until we run full_clean
            new_pokemon.full_clean()
            # here we will ensure our instance is actually created
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            print(e.message_dict)
            #if it sends an error we want to ensure this test fails
            self.fail()

    def test_02_create_pokemon_with_incorrect_name_format(self):
        new_pokemon = Pokemon(name = 'lucari0', description = 'Looks like a puppy, but its just a ditto')
        try:
            new_pokemon.full_clean()
            # if our instance runs through the full clean and doesn't throw an error, than we
            # know our validator is not working correctly and we should fail this test 
            self.fail()
        except ValidationError as e:
            self.assertTrue('Improper name format.' in e.message_dict['name'])