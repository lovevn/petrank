from django.shortcuts import render, redirect, get_object_or_404
from pets.models import Pet

def root(request):

    pets = Pet.objects.order_by("?").all()[:2]
    return render(request, "home.html", {"pets": pets})
