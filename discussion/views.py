
#from xml.etree.ElementTree import Comment
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from discussion.models import ImagePost, Discussion, Comment



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
    fields = ['title', 'subtitle', 'image', 'description']

# Si la forma es valida, el usuario podrá crear la 
# discusión a su nombre
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DiscussionUpdateView(LoginRequiredMixin, UpdateView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')
    fields = ['title', 'subtitle', 'image', 'description']


class DiscussionDeleteView(LoginRequiredMixin, DeleteView):
    model = Discussion
    success_url = reverse_lazy('discussion:discussion-list')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "discussion/add_comment.html"
    fields = ['description']
    success_url = "/discussion/discussion/{discussion_id}/detail"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.discussion_id = self.kwargs['pk']
        return super().form_valid(form)


def get_image_url_ctx(request):
    image = ImagePost.objects.filter(discussion=request.discussion.id)
    if image.exists():
        return {"url": image[0].image.url}
    return {}
