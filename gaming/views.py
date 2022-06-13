
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from gaming.models import Gaming

class GamingListView(ListView):
    model = Gaming
    template_name = "gaming/gaming_list.html"


class GamingDetailView(DetailView):
    model = Gaming
    template_name = "gaming/gaming_detail.html"
    fields = ['name', 'platform', 'description']


class GamingCreateView(LoginRequiredMixin, CreateView):
    model = Gaming
    success_url = reverse_lazy('gaming:gaming-list')
    fields = ['name', 'platform', 'description']


class GamingUpdateView(LoginRequiredMixin, UpdateView):
    model = Gaming
    success_url = reverse_lazy('gaming:gaming-list')
    fields = ['name', 'platform', 'description']


class GamingDeleteView(LoginRequiredMixin, DeleteView):
    model = Gaming
    success_url = reverse_lazy('gaming:gaming-list')
