from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView

class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'members/register.html'
