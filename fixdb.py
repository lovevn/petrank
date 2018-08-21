import sys
import os
sys.path.append(os.path.join("..", "core"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django; django.setup()
from django.db import transaction
from django.core.management import call_command
from pets.models import *

print("This will destroy the database! Press '1' to continue")
if input() != "1": exit()

# 1. Website should be down!

# 2. Make copy of everything!

# 2. Get full history
snapshots = PetSnapshot.objects.all().order_by("datetime")
history = []
for s in list(snapshots):
    if not s.lost_against and not s.won_against:
        history.append(["CREATION", s.datetime, s.pet.id, s.pet.name,
         s.pet.owner, s.pet.species, s.pet.mediafile.name, s.pet.verified])
    elif not s.lost_against:
        history.append(["VICTORY", s.datetime, s.pet.id, s.won_against.id])
    else:
        history.append(["DEFEAT", s.datetime, s.pet.id, s.lost_against.id])


# 3. Delete records
for s in snapshots: s.delete()
for p in Pet.objects.all(): p.delete()

# 4. Reinstate
for event in history:
    if event[0] == "CREATION":
        pet = Pet.objects.create(
         id=event[2], name=event[3], owner=event[4], species=event[5],
         mediafile=event[6], verified=event[7]
        )
        PetSnapshot.objects.create(
         pet=pet, datetime=event[1],
         ranking=pet.ranking()[0], elo_rating=pet.elo_rating
        )
    elif event[0] == "VICTORY":
        winner = Pet.objects.get(id=event[2])
        loser = Pet.objects.get(id=event[3])
        winner.defeat(loser)
        s = winner.petsnapshot_set.last()
        s.datetime = event[1]
        s.save()
        s = loser.petsnapshot_set.last()
        s.datetime = event[1]
        s.save()
