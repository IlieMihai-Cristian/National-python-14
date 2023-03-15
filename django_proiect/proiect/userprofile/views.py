from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from userprofile.forms import NewAccountForm


# Create your views here.

class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/locations_form.html'
    # fields = ['first_name', 'last_name', 'username', 'email']
    form_class = NewAccountForm

