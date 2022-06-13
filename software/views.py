
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from software.models import Software

class SoftwareListView(ListView):
    model = Software
    template_name = "software/software_list.html"


class SoftwareDetailView(DetailView):
    model = Software
    template_name = "software/software_detail.html"
    fields = ['name', 'type', 'description']


class SoftwareCreateView(LoginRequiredMixin, CreateView):
    model = Software
    success_url = reverse_lazy('software:software-list')
    fields = ['name', 'type', 'description']


class SoftwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Software
    success_url = reverse_lazy('software:software-list')
    fields = ['name', 'type', 'description']


class SoftwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Software
    success_url = reverse_lazy('software:software-list')
