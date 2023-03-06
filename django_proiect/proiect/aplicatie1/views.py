from django.shortcuts import render
from django.views.generic import ListView

from aplicatie1.models import Location


# CreateView -> adaugarea datelor in baza de date (instante noi)
# DetailView -> vizualizarea datelor unei instante din baza de date (furnizez pk)
# ListView -> vizualizarea datelor mai multor instante din baza de date
# UpdateView -> modificarea datelor din baza de date (furnizez pk)
# DeleteView -> stergerea datelor din baza de date (furnizez pk)

class LocationsView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'
