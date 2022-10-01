from .models import Comment, Reservation, Contact
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


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
            'date': DatePickerInput(format='%d-%m-%Y'),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


