from django.shortcuts import render, redirect, get_object_or_404

def root(request):
    return render(request, "home.html")
