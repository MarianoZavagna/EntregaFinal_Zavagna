from django.shortcuts import render
from django.db.models import Q

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
