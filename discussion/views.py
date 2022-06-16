
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from discussion.models import ImagePost, Discussion


from discussion.models import Discussion

class DiscussionListView(ListView):
    model = Discussion
    template_name = "discussion/discussion_list.html"


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = "discussion/discussion_detail.html"
    fields = ['title', 'image', 'description']


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
    fields = ['title', 'image', 'description']


class DiscussionUpdateView(LoginRequiredMixin, UpdateView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
    fields = ['title', 'image', 'description']


class DiscussionDeleteView(LoginRequiredMixin, DeleteView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')


def get_image_url_ctx(request):
    image = ImagePost.objects.filter(discussion=request.discussion.id)
    if image.exists():
        return {"url": image[0].image.url}
    return {}
