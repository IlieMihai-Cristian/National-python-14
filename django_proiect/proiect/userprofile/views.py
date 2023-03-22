import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView

from userprofile.forms import NewAccountForm


# Create your views here.

class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/locations_form.html'
    # fields = ['first_name', 'last_name', 'username', 'email']
    form_class = NewAccountForm

    # def get_object(self, queryset=None):
    #     print(self.object)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + '!$%?#@') for _ in range(8))
        # print(self.object.id)
        if User.objects.filter(id=self.object.id).exists():
            user_instance = User.objects.get(id=self.object.id)
        # if (user_instance := User.objects.get(id=self.object.id)) and user_instance.exists():
            user_instance.set_password(psw)
            user_instance.save()
            content = f'Datele de autentificare sunt: \n {user_instance.username} \n {psw}'
            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='date conectare aplicatie', body=content,
                                           from_email='contact@test.ro', to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('locations:lista_locatii')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
