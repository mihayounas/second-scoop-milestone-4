from django.test import TestCase
from .models import Comment
from .forms import CommentForm

# Create your tests here.


class CommentTestCase(TestCase):
    def test_name_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid)
        self.asesertIn('body', forms.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required')
    


