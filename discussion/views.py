
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from discussion.models import Discussion

class DiscussionListView(ListView):
    model = Discussion
    template_name = "discussion/discussion_list.html"


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = "discussion/discussion_detail.html"
    fields = ['title', 'platform', 'description']


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
    fields = ['title', 'platform', 'description']


class DiscussionUpdateView(LoginRequiredMixin, UpdateView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
    fields = ['title', 'platform', 'description']


class DiscussionDeleteView(LoginRequiredMixin, DeleteView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
