from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from annoying.decorators import render_to

from .models import Item
from .forms import SaleForm


class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SaleForm
        return context


class ItemSaleFormView(SingleObjectMixin, FormView):
    template_name = 'item_detail.html'
    form_class = SaleForm
    model = Item

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('item_detail', kwargs={'slug': self.slug})


class ItemView(View):

    def get(self, request, *args, **kwargs):
        view = ItemDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ItemSaleFormView.as_view()
        return view(request, *args, **kwargs)


# @render_to('base.html')
# def index(request):
#     return {}

def index(request):
    items = Item.objects.all()
    return render(request, 'base.html', {'items': items})
