from unittest.mock import patch, Mock, MagicMock, PropertyMock
from testarsenal import DjangoTest
from django.core.files.uploadedfile import SimpleUploadedFile
from pets.models import *

class PetTests(DjangoTest):

    def setUp(self):
        media_file = SimpleUploadedFile("test.png", b"\x00\x01\x02\x03")
        self.kwargs = {"mediafile": media_file}


    def test_can_create_pet(self):
        pet = Pet(**self.kwargs)
        pet.full_clean(), pet.save()
        self.assertEqual(pet.species, "Cat")
        self.assertEqual(pet.elo_rating, 1000)
        self.assertFalse(pet.verified)


    def test_pet_combat(self):
        pet1 = Pet(**self.kwargs)
        pet2 = Pet(**self.kwargs)
        pet1.defeat(pet2)
        self.assertEqual(pet1.elo_rating, 1015)
        self.assertEqual(pet2.elo_rating, 985)
        pet2.defeat(pet1)
        self.assertEqual(round(pet1.elo_rating), 999)
        self.assertEqual(round(pet2.elo_rating), 1001)
        pet1 = Pet(**self.kwargs, elo_rating=1100)
        pet2 = Pet(**self.kwargs, elo_rating=2500)
        pet2.defeat(pet1)
        pet1 = Pet(**self.kwargs, elo_rating=1100)
        pet2 = Pet(**self.kwargs, elo_rating=2500)
        pet1.defeat(pet2)
