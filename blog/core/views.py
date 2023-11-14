from django.shortcuts import render
from .forms import UniForm
# Create your views here.
def index(request):
    return render(request, 'core/index.html', {'form': UniForm()})

