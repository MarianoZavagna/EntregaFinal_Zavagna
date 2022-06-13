
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from hardware.models import Hardware

class HardwareListView(ListView):
    model = Hardware
    template_name = "hardware/hardware_list.html"


class HardwareDetailView(DetailView):
    model = Hardware
    template_name = "hardware/hardware_detail.html"
    fields = ['name', 'category', 'description']


class HardwareCreateView(LoginRequiredMixin, CreateView):
    model = Hardware
    success_url = reverse_lazy('hardware:hardware-list')
    fields = ['name', 'category', 'description']


class HardwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Hardware
    success_url = reverse_lazy('hardware:hardware-list')
    fields = ['name', 'category', 'description']


class HardwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Hardware
    success_url = reverse_lazy('hardware:hardware-list')
