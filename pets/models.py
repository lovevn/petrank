"""Pet models."""

import random
from datetime import datetime
from django.db import models

class Pet(models.Model):
    """Represents a pet image."""

    class Meta:
        db_table = "pets"

    mediafile = models.FileField()
    species = models.CharField(
     max_length=16,
     choices=(("PUSS", "Cat"), ("DOGGO", "Dog")),
     default="PUSS"
    )
    elo_rating = models.IntegerField(default=1000)
    verified = models.BooleanField(default=False)


    @staticmethod
    def create_from_file(file, species="PUSS"):
        pet = Pet.objects.create(mediafile=file, species=species)
        PetSnapshot.objects.create(
         datetime=datetime.now(),
         pet=pet,
         elo_rating=pet.elo_rating
        )
        return pet


    @staticmethod
    def two_random_images(species):
        pets = list(Pet.objects.filter(species=species, verified=True))
        if len(pets) < 2: pets = [None, None]
        pet1 = random.choice(pets)
        pets.remove(pet1)
        pet2 = random.choice(pets)
        return [pet1, pet2]


    def defeat(self, loser):
        winner_prob = (1.0 / (1.0 + pow(10, ((self.elo_rating-loser.elo_rating) / 400))))
        loser_prob = (1.0 / (1.0 + pow(10, ((loser.elo_rating-self.elo_rating) / 400))))

        self.elo_rating = self.elo_rating + (30 * (1 - winner_prob))
        loser.elo_rating = loser.elo_rating + (30 * (0 - winner_prob))
        self.save()
        loser.save()

        PetSnapshot.objects.create(
         datetime=datetime.now(),
         pet=self,
         elo_rating=self.elo_rating
        )
        PetSnapshot.objects.create(
         datetime=datetime.now(),
         pet=loser,
         elo_rating=loser.elo_rating
        )


    def ranking(self):
        pets = list(Pet.objects.filter(species=self.species, verified=True).order_by("-elo_rating"))
        if self.verified:
            return pets.index(self) + 1, len(pets)
        else:
            return [0, len(pets)]



class PetSnapshot(models.Model):
    """A snapshot of a pet's rating at a given time."""

    class Meta:
        db_table = "pet_snapshots"

    datetime = models.DateTimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    elo_rating = models.IntegerField()
