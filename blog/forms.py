from .models import Comment, Reservation
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date',)
