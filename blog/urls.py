from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="home"),
    path("<slug:slug>/", views.ReadMore.as_view(), name="read_more"),
    path("genre/<slug:slug>/", views.genre_detail, name="genre_detail"),
    path("events/<slug:slug>/", views.events_view, name="upcoming_events"),
]
