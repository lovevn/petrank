"""The core views."""

import random
from django.shortcuts import render, redirect, get_object_or_404
from pets.models import Pet

def home(request):
    """The home page."""

    if request.method == "POST":
        winner = Pet.objects.get(id=request.POST["winner"])
        loser = Pet.objects.get(id=request.POST["loser"])
        # Calculate probabilities
        winner_prob = (1.0 / (1.0 + pow(10, ((winner.elo_rating-loser.elo_rating) / 400))))
        loser_prob = (1.0 / (1.0 + pow(10, ((loser.elo_rating-winner.elo_rating) / 400))))

        winner.elo_rating = winner.elo_rating + (30 * (1 - winner_prob))
        loser.elo_rating = loser.elo_rating + (30 * (0 - winner_prob))
        winner.save()
        loser.save()
        return redirect("/")
    pets = list(Pet.objects.all())
    pet1 = random.choice(pets)
    pets.remove(pet1)
    pet2 = random.choice(pets)
    return render(request, "home.html", {"pets": [pet1, pet2]})
