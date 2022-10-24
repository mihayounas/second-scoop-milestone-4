from django.test import TestCase
from .models import Reservation
from .forms import Booking

# Create your tests here.


# class TestPost(TestCase):


# class TestComment(TestCase):


# class TestContact(TestCase):


class ReservationsTestCase(TestCase):
    def test_name_required(self):
        form = Booking({'phone': ''})
        self.assertFalse(form.is_valid())
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = Booking()
        self.assertEqual(form.Meta.fields, ['name', 'phone',
                  'event', 'date', 'number_of_people', 'message'])
