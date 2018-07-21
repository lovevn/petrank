import random
from django.shortcuts import render, redirect, get_object_or_404
from pets.models import Pet

def root(request):
    if request.method == "POST":
        return redirect("/")
    pets = list(Pet.objects.all())
    pet1 = random.choice(pets)
    pets.remove(pet1)
    pet2 = random.choice(pets)
    return render(request, "home.html", {"pets": [pet1, pet2]})
