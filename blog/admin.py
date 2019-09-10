from django.contrib import admin
from .models import Post, Genre, Event, Employee

admin.site.register(Post)
admin.site.register(Genre)
admin.site.register(Event)
admin.site.register(Employee)
