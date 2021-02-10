from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario

class UsuarioRegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Password 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password 2', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'first_name', 'last_name')

    def Clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não coincidem')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user