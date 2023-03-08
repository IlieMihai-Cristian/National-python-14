from django.urls import path
from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationsView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateLocationsView.as_view(), name='modificare'),
    path('<int:pk>/delete/', views.delete_location, name='stergere'),
    path('<int:pk>/activate/', views.activate_location, name='activare'),
]