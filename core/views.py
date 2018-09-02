"""The core views."""

from django.shortcuts import render, redirect, get_object_or_404
import random
import subprocess
from .secrets import email
from pets.models import Pet

def home(request):
    """The home page."""

    if not request.GET:
        return redirect("/?s=" + random.choice(["Cat", "Dog", "Other"]))
    species = request.GET["s"] if request.GET else "Cat"
    if request.method == "POST":
        winner = Pet.objects.get(id=request.POST["winner"])
        loser = Pet.objects.get(id=request.POST["loser"])
        winner.defeat(loser)
        return redirect("/?s=" + species + "#choices")
    pets = Pet.two_random_images(species)
    return render(request, "home.html", {"pets": pets, "species": species})


def terms(request):
    return render(request, "terms.html")


def help(request):
    return render(request, "help.html")


def upload(request):
    if request.method == "POST":
        pet = Pet.create_from_file(request)
        subprocess.call("convert {} -auto-orient {}".format(
         pet.mediafile.path, pet.mediafile.path
        ), shell=True)
        subprocess.call("chmod 744 {}".format(pet.mediafile.path), shell=True)
        email(pet, request.scheme + "://" + request.get_host())
        return redirect("/pets/{}/".format(pet.id))
    return render(request, "upload.html")


def not_found(request, exception):
    return redirect("/")
