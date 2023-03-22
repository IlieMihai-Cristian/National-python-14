from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

    def clean(self):
        field_data = self.cleaned_data
        print(self.data)
        print(self.fields)
        print(self.fields['email'])
        # print(field_data)
        email_value = field_data.get('email')
        if User.objects.filter(email=email_value).exists():
            msg = ''
            msg = 'Emailul deja exista! te rugam sa adaugi un alt email'
            self._errors['email'] = self.error_class([msg])
        return field_data
