"""Pet specific views."""

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Pet, PetSnapshot

def pet(request, id):
    """The view to look at a particular pet image and its stats."""

    try:
        pet = get_object_or_404(Pet, id=id)
    except ValueError: raise Http404()
    snapshots = PetSnapshot.objects.filter(pet=pet)

    time_data = [[int(s.datetime.strftime('%s')) * 1000, s.elo_rating] for s in snapshots]
    if time_data: time_data += [[int(datetime.now().strftime('%s')) * 1000, time_data[-1][1]]]
    data = [d[1] for d in time_data[:-1]]
    time_rank_data = [[int(s.datetime.strftime('%s')) * 1000, s.ranking] for s in snapshots if s.ranking != 0]
    if time_rank_data:
        time_rank_data += [[int(datetime.now().strftime('%s')) * 1000, time_rank_data[-1][1]]]
    else:
        time_rank_data = [[int(datetime.now().strftime('%s')) * 1000, 0]]
    rank_data = [d[1] for d in time_rank_data[:-1]]
    print(time_rank_data)
    defeats = [s.lost_against.name if s.lost_against else "" for s in snapshots]
    wins = [s.won_against.name if s.won_against else "" for s in snapshots]
    return render(request, "pet.html", {
     "pet": pet, "time_data": time_data, "data": data, "defeats": defeats,
     "time_rank_data": time_rank_data, "rank_data": rank_data, "wins": wins})


def pets(request):
    dogs = Pet.objects.filter(species="Dog", verified=True).order_by("-elo_rating")
    cats = Pet.objects.filter(species="Cat", verified=True).order_by("-elo_rating")
    other = Pet.objects.filter(species="Other", verified=True).order_by("-elo_rating")
    return render(request, "pets.html", {"lists": [[dogs, "DOGGOS"], [cats, "CATS"], [other, "OTHER"]]})
