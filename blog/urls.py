from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("<str:slug>/", views.ReadMore.as_view(), name="read_more"),
    path("genre/<slug:slug>/", views.genre_detail, name="genre_detail"),
    path("events/<slug:slug>/", views.EventsView.as_view(), name="upcoming_events"),
    path("contact", views.contact_view, name="contact"),
]
