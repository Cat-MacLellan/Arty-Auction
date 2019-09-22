from django.shortcuts import render
from art.models import Art

# Create your views here.
def do_search(request):
    art = Art.objects.filter(name__icontains=request.GET['q'])
    return render(request, "art.html", {"art": art})