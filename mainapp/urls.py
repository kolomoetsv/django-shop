from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/$', views.ItemsListView.as_view(), name='items'),
    url(r'^(?P<slug>[\w-]+)/$', views.ItemDetailView.as_view(), name='item-detail'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<slug:slug>/', ItemDetailView.as_view(), name='item-detail'),
# ]