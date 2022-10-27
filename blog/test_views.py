from django.test import TestCase

# Test views for the first page


class TestViews(TestCase):
    def test_the_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './homepage.html')

    def test_the_get_slide_of_the_first_pg(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

# test error 404 page 
    def test_404_page(self):
        response = self.client.get('/5jtnn')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'error.html')
