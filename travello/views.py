from django.shortcuts import render
from .models import Destination

def index(request):
    # Create each destination instance and set attributes one by one
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
