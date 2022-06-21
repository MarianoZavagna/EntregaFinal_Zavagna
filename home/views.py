from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView
from discussion.models import Discussion
from user.models import Avatar



def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    discussions = Discussion.objects.all()
    context_dict.update({
        'discussions': discussions,
    })
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(title__contains=search_param)
        #query.add(Q(platform__contains=search_param), Q.OR)
        discussions = Discussion.objects.filter(query)
        context_dict.update({
            'discussions': discussions,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )


def about(request):
    return render(request, "home/about.html")


def policy(request):
    return render(request, "home/policy.html")


def terms(request):
    return render(request, "home/terms.html")


class Error404View(TemplateView):
    template_name = 'home/not_found.html'


class Error505View(TemplateView):
    template_name = 'home/not_found.html'

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view

