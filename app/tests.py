from django.test import TestCase
from .models import Images
from django.urls import reverse
from media import media


class ImagesPageViewTest(TestCase):
    def setUp(self):
        Images.objects.create(title = 'hi', image = 'file.jpg', text = 'test')  

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home_url'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_url_by_name(self):
        response = self.client.get(reverse('about_url'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_url_by_name(self):
        response = self.client.get(reverse('gallery_url'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_view_url_by_name(self):
        response = self.client.get(reverse('contacts_url'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/home.html')

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/about.html')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('gallery_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/gallery.html')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contacts_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contacts.html')