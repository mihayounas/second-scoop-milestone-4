from django.test import TestCase
from .models import Reservation
from .forms import Booking

# Create your tests here.


class ReservationsTestCase(TestCase):
    def test_name_required(self):
        form = Booking({'phone': ''})
        self.assertFalse(form.is_valid())
        self.asesertIn('phone', forms.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'Please fill in this field.')
