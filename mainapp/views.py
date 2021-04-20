from django.shortcuts import render
from django.views import generic
from . import models


class ItemsListView(generic.ListView):
    model = models.Item


class ItemDetailView(generic.DetailView):
    model = models.Item
    template_name = 'item_detail.html'


def index(request):
    return render(request, 'base.html', {})
