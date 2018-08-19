"""The core views."""

from django.shortcuts import render, redirect, get_object_or_404
from pets.models import Pet

def home(request):
    """The home page."""

    species = request.GET["s"] if request.GET else "Cat"
    if request.method == "POST":
        if "file" in request.FILES:
            pet = Pet.create_from_file(
             file=request.FILES["file"],
             species=species
            )
            return redirect("/pets/{}/".format(pet.id))
        else:
            winner = Pet.objects.get(id=request.POST["winner"])
            loser = Pet.objects.get(id=request.POST["loser"])
            winner.defeat(loser)
            return redirect("/?s=" + species + "#choices")
    pets = Pet.two_random_images(species)
    return render(request, "home.html", {"pets": pets, "species": species})


def terms(request):
    return render(request, "terms.html")


def not_found(request, exception):
    return redirect("/")
