from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie1.models import Location


# CreateView -> adaugarea datelor in baza de date (instante noi)
# DetailView -> vizualizarea datelor unei instante din baza de date (furnizez pk)
# ListView -> vizualizarea datelor mai multor instante din baza de date
# UpdateView -> modificarea datelor din baza de date (furnizez pk)
# DeleteView -> stergerea datelor din baza de date (furnizez pk)

class LocationsView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'


class CreateLocationsView(CreateView):
    model = Location
    template_name = 'aplicatie1/locations_form.html'
    fields = ['city', 'country']

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationsView(UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


def delete_location(request, pk):
    """
    SQL native query: SELECT id, city FROM aplicatie1_location WHERE id=1
    Django query: Location.objects.get(id=1).id

    model.objects.get(coloana1=val1, coloana2=val2) -> returneaza o singura inregistrare
                -> daca nu exista inregistrarea cautata in db sau exista mai multe inregistrari in db care contin
                aceeasi valoare a parametrilor din get, va returna eroare (recomandat este sa fie folosit ca si param. id-ul)
                -> avand in vedere ca returneaza o singura inregistrare (obiect) putem sa accesam direct atributul
                (proprietatea, field-ul din db): model.objects.get(id=1).city
    models.object.filter(coloana1=val1, coloana2=val2) -> returneaza 1 sau mai multe inregistrari
                -> ca sa accesez atributele (field-urile) pot sa:
                    - fie iteram prin rezultate
                    - fie sa scriu model.objects.filter().values()
                    - fie sa scriu model.objects.filter().values_list('city')
    @type request:
    @param pk:
    """
    # folosind get
    # instance_object = Location.objects.get(id=pk)
    # if instance_object.active:
    #     instance_object.active = False
    #     instance_object.save()

    # folsind filter
    Location.objects.filter(id=pk).update(active=False)
    return redirect('locations:lista_locatii')


def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect('locations:lista_locatii')