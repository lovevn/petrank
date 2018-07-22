"""The core views."""

import random
from django.shortcuts import render, redirect, get_object_or_404
from pets.models import Pet

def home(request):
    """The home page."""

    species = request.GET["s"] if request.GET else "PUSS"

    if request.method == "POST":
        if "file" in request.FILES:
            Pet.objects.create(
             mediafile=request.FILES["file"]
            )
            return redirect("/pets/")
        else:
            winner = Pet.objects.get(id=request.POST["winner"])
            loser = Pet.objects.get(id=request.POST["loser"])
            # Calculate probabilities
            winner.defeat(loser)
            return redirect("/?s=" + species)
    pets = list(Pet.objects.filter(species=species))
    if len(pets) < 2: pets = [None, None]
    pet1 = random.choice(pets)
    pets.remove(pet1)
    pet2 = random.choice(pets)
    return render(request, "home.html", {"pets": [pet1, pet2], "species": species})

def terms(request):
    return render(request, "terms.html")
