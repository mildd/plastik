from django.views import generic
from django.views.generic import View
from .models import *
from django.shortcuts import render
from .utils import MixinObject
from .forms import MessageForm


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
    employees = Employee.objects.all
    if request.method == 'post':
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            mes = 'Your message has been send!'
            return render(request, 'contact.html', {'employees': employees, 'form': form, 'mes': mes})
        else:
            form = MessageForm()
            return render(request, 'contact.html', {'employees': employees, 'form': form})

