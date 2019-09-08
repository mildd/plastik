from django.views import generic
from .models import Post, Genre, Event
from django.shortcuts import render


def index_view(request):
    posts = Post.objects.all()
    genres = Genre.objects.all()
    events = Event.objects.all()
    return render(request, "index.html", context={"posts": posts, "genres": genres, "events": events})


class ReadMore(generic.DetailView):
    model = Post
    template_name = "read_more.html"


def genre_detail(request, slug):
    genres = Genre.objects.all()
    genre = Genre.objects.get(slug__iexact=slug)
    return render(request, "genre_detail.html", context={"genre": genre, "genres": genres})


def events_view(request, slug):
    events = Event.objects.all()
    event = Event.objects.get(slug__iexact=slug)
    return render(request, "upcoming_events.html", context={"events": events, "event": event})

