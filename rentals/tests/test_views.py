from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rentals.models import Flat, City

#view test examples
class searchTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_city = City.objects.create( name = 'Warszawa')
        Flat.objects.create(id= '5cadf422-c9b4-4e1c-abcb-88203f2df712', city = new_city, adress = 'Bootstrapowa 42', prize = 1500, deposit = True, description = 'Flat is comfortable')


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('searching_panel', args ={'cityname': 'Warszawa'}))
        self.assertEqual(response.status_code, 200)

class FlatDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_city = City.objects.create( name = 'Warszawa')
        jpg_file = SimpleUploadedFile(name='room1.jpg', content=open('flats/media/media/room1.jpg', 'rb').read(), content_type='image/jpeg')
        Flat.objects.create(id= 'bb9fddb4-037f-4fa4-9ce9-2c8732686a01', city = new_city, adress = 'Phpowa 42', prize = 1000, deposit = False, description = 'Flat is big and comfortable', photo = jpg_file)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('flat_detail', kwargs ={'pk': 'bb9fddb4-037f-4fa4-9ce9-2c8732686a01'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/flat_detail.html')
