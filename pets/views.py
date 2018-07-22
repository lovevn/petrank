"""Pet specific views."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet

def pet(request, id):
    """The view to look at a particular pet image and its stats."""

    pet = get_object_or_404(Pet, id=id)
    return render(request, "pet.html", {"pet": pet})


def pets(request):
    pets = Pet.objects.order_by("-elo_rating")
    return render(request, "pets.html", {"pets": pets})
