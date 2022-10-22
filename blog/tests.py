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
