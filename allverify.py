import sys
import os
sys.path.append(os.path.join("..", "petrank"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django; django.setup()
from django.db import transaction
from pets.models import Pet

for pet in Pet.objects.all():
    pet.verified = True
    pet.save()
