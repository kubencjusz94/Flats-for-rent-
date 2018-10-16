import datetime

from django.test import TestCase
from django.utils import timezone
from  rentals.forms import SearchModelForm

#form test examples
class SearchModelFormTest(TestCase):

    def test_search_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = SearchModelForm(data={'date_of_rent': date})
        self.assertFalse(form.is_valid())
