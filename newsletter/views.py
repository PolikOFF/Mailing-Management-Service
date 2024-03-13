from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from newsletter.models import Sending, Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('fio', 'email', )
    success_url = reverse_lazy('newsletter:list_client')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
