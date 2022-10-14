from .models import Comment, Reservation, Contact, Post
from django import forms
from datetime import datetime
from django.contrib.admin import widgets


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'


class Booking(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'phone',
                  'event', 'date', 'number_of_people', 'message')
        widgets = {
            'date': DateInput(),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'slug', 'content')
