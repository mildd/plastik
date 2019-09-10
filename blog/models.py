from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(unique=True)
    released = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField("Genre", blank=True, related_name="posts")
    image = models.ImageField(upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("read_more", kwargs={'slug': self.slug})


class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={'slug': self.slug})


class Event(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(unique=True)
    image = models.ImageField(upload_to="images/")
    date = models.DateTimeField()
    place = models.CharField(max_length=50)
    line_up = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vk_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("upcoming_events", kwargs={'slug': self.slug})


class Employee(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image/")
    description = models.TextField()
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact", kwargs={"slug": self.slug})
