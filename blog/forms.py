from .models import Comment, Reservation
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
