from django.shortcuts import render
from django.views import generic
from . import models
from annoying.decorators import render_to
from .models import Item, Employee

class ItemsListView(generic.ListView):
    model = models.Item


class ItemDetailView(generic.DetailView):
    model = models.Item
    template_name = 'item_detail.html'


# @render_to('base.html')
# def index(request):
#     return {}

def index(request):
    items = Item.objects.all()
    return render(request, 'base.html', {'items': items})
