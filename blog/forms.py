from .models import Comment, Reservation, CreatePost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class Booking(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'phone',
                  'event', 'date', 'message')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class NewPost(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = {'title', 'content', 'img_field'}
