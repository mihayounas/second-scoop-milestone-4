from .models import Comment, Reservation, Contact
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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
