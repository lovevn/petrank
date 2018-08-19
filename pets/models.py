"""Pet models."""

import random
from datetime import datetime
from django.db import models

class Pet(models.Model):
    """Represents a pet image."""

    class Meta:
        db_table = "pets"
        ordering = ["verified"]


    def create_filename(instance, filename):
        extension = "." + filename.split(".")[-1] if "." in filename else ""
        return datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S") + extension


    mediafile = models.FileField(upload_to=create_filename)
    species = models.CharField(
     max_length=16,
     choices=(("Cat", "Cat"), ("Dog", "Dog")),
     default="Cat"
    )
    elo_rating = models.IntegerField(default=1000)
    verified = models.BooleanField(default=False)
    name = models.CharField(max_length=256, default="Anonymous")
    owner = models.CharField(max_length=256, default="Anonymous")

    def __str__(self):
        return "<Pet ({}): {}verified {}>".format(
         self.id, "" if self.verified else "un", self.species
        )


    @staticmethod
    def create_from_file(request):
        pet = Pet.objects.create(mediafile=request.FILES["file"], species=request.POST["species"])
        if request.POST["name"]: pet.name = request.POST["name"]
        if request.POST["owner"]: pet.owner = request.POST["owner"]
        pet.save()
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
        """Defeat another Pet and update ELO rankings accordingly."""
        
        r1 = 10 ** (self.elo_rating / 400)
        r2 = 10 ** (loser.elo_rating / 400)
        e1 = r1 / (r1 + r2)
        e2 = r2 / (r1 + r2)
        self.elo_rating = self.elo_rating + (30 * (1 - e1))
        loser.elo_rating = loser.elo_rating + (30 * (0 - e2))
        self.save()
        loser.save()

        PetSnapshot.objects.create(
         datetime=datetime.now(),
         pet=self,
         elo_rating=self.elo_rating,
         won_against=loser
        )
        PetSnapshot.objects.create(
         datetime=datetime.now(),
         pet=loser,
         elo_rating=loser.elo_rating,
         lost_against=self
        )


    def ranking(self):
        """The position of the pet among all verified pets, ordered by ELO
        rating."""

        pets = list(Pet.objects.filter(
         species=self.species, verified=True
        ).order_by("-elo_rating"))
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
    won_against = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_won_against')
    lost_against = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_lost_against')
