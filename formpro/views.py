from django.shortcuts import render
from .models import ContactForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy


class FormCreateView(CreateView):
    model = ContactForm
    template_name = 'form_new.html'
    fields = ('name','family_name','telephone_number','email','message')


class ContactListView(ListView):
    model = ContactForm
    template_name = 'contact_list.html'