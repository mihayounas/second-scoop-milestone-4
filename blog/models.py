from django.db import models
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
import datetime
from django.core.validators import RegexValidator, MinValueValidator


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='post_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_view')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        return reverse('post_detail')


class Profile(models.Model):
    user_profile = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, default='1')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservation_request", null=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False, validators=[MinValueValidator(datetime.date.today), RegexValidator(
        "(\d{4})-(\d{2})-(\d{2})"
    )])
    phone = models.CharField(max_length=11, validators=[RegexValidator(
        "^((\+44)|(0)) ?\d{4} ?\d{6}$"
    )])
    number_of_people = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])
    event = models.CharField(max_length=100)
    message = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservations_view')


class Contact(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact_message", null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    reply = models.TextField()
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('message_list')
