from django.views import generic
from django.views.generic import View
from .models import *
from django.shortcuts import render
from .utils import MixinObject


def index_view(request):
    posts = Post.objects.all()
    genres = Genre.objects.all()
    events = Event.objects.all()
    return render(request, "index.html", context={"posts": posts, "genres": genres, "events": events})


class ReadMore(MixinObject, View):
    model = Post
    template = "read_more.html"


def genre_detail(request, slug):
    genres = Genre.objects.all()
    genre = Genre.objects.get(slug__iexact=slug)
    return render(request, "genre_detail.html", context={"genre": genre, "genres": genres})


class EventsView(generic.DetailView):
    model = Event
    template_name = "upcoming_events.html"


def contact_view(request):
    employees = Employee.objects.all()
    return render(request, "contact.html", context={"employees": employees})
