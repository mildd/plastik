from django.views import generic
from django.views.generic import View
from .models import *
from django.shortcuts import render
from .utils import MixinObject
from .forms import MessageForm, ResponseForm


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
    events = Event.objects.all()
    genre = Genre.objects.get(slug__iexact=slug)
    return render(request, "genre_detail.html", context={"genre": genre, "genres": genres, 'events': events})


class EventsView(generic.DetailView):
    model = Event
    template_name = "upcoming_events.html"


def contact_view(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            mes = "Your message has been send!"
            return render(request, "contact.html", {'employees': employees, 'form': form, 'mes': mes})
    else:
        form = MessageForm()
        return render(request, "contact.html", {'employees': employees, 'form': form})


def about_view(request):
    responses = Response.objects.all()
    abouts = About.objects.all()
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            mes = "Your response has been send!"
            return render(request, 'about.html', {'abouts': abouts, 'form': form, 'responses': responses, 'mes': mes})
    else:
        form = ResponseForm()
        return render(request, 'about.html', {'abouts': abouts, 'form': form, 'responses': responses})
