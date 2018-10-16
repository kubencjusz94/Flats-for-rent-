from django.test import TestCase

from rentals.models import City, Flat

#model test examples
class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        City.objects.create( name = 'Warszawa')

    def test_name_label(self):
        city = City.objects.get(id = 1)
        field_label = city._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        city = City.objects.get(id = 1)
        max_length = city._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

class FlatModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_city = City.objects.create( name = 'Warszawa')
        Flat.objects.create(id= '5cadf422-c9b4-4e1c-abcb-88203f2df712', city = new_city, adress = 'Bootstrapowa 42', prize = 1500, deposit = True, description = 'Flat is comfortable')

    def test_get_absolute_url(self):
        flat = Flat.objects.get(adress = 'Bootstrapowa 42')
        self.assertEquals(flat.get_absolute_url(), '/rentals/flat%20/5cadf422-c9b4-4e1c-abcb-88203f2df712/')
