"""Pet specific views."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet, PetSnapshot

def pet(request, id):
    """The view to look at a particular pet image and its stats."""

    pet = get_object_or_404(Pet, id=id)
    snapshots = PetSnapshot.objects.filter(pet=pet)
    data = [[int(s.datetime.strftime('%s')) * 1000, s.elo_rating] for s in snapshots]
    return render(request, "pet.html", {"pet": pet, "data": data})


def pets(request):
    dogs = Pet.objects.filter(species="DOGGO", verified=True).order_by("-elo_rating")
    cats = Pet.objects.filter(species="PUSS", verified=True).order_by("-elo_rating")
    return render(request, "pets.html", {"lists": [[dogs, "HECKING DOGGOS"], [cats, "SWEET PUSS"]]})
