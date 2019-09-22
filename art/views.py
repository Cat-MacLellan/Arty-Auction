from django.shortcuts import render
from .models import Art

# Create your views here.
def all_art(request):
    art = Art.objects.all()
    return render(request, "art.html", {"art": art})