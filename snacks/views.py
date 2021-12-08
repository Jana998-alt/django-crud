from django.db import models
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "detail_template.html"
    model = Snack

class SnackCreateView(CreateView):
    template_name = "create_template.html"
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = "update_template.html"
    model = Snack

class SnackDeleteView(DeleteView):
    template_name = "delete_template.html"
    model = Snack