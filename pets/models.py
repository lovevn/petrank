"""Pet models."""

from django.db import models

class Pet(models.Model):
    """Represents a pet image."""

    class Meta:
        db_table = "pets"

    url = models.URLField(unique=True)
