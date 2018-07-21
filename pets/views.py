from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet

def pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    return render(request, "pet.html", {"pet": pet})
