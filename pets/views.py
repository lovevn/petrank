"""Pet specific views."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet

def pet(request, id):
    """The view to look at a particular pet image and its stats."""

    pet = get_object_or_404(Pet, id=id)
    return render(request, "pet.html", {"pet": pet})


def pets(request):
    dogs = Pet.objects.filter(species="DOGGO").order_by("-elo_rating")
    cats = Pet.objects.filter(species="PUSS").order_by("-elo_rating")
    return render(request, "pets.html", {"lists": [[dogs, "HECKING DOGGOS"], [cats, "SWEET PUSS"]]})
