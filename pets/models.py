"""Pet models."""

from django.db import models

class Pet(models.Model):
    """Represents a pet image."""

    class Meta:
        db_table = "pets"

    url = models.URLField(unique=True)
    species = models.CharField(
     max_length=16,
     choices=(("PUSS", "Cat"), ("DOGGO", "Dog")),
     default="PUSS"
    )
    elo_rating = models.IntegerField(default=1000)
