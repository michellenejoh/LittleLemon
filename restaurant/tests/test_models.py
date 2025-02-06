from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="cheese", price=8, inventory=100)
        self.assertEqual(str(item), "cheese : 8")