from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
view = MenuItemsView.as_view()


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Biriyani', price=220, inventory=100)
        Menu.objects.create(title='Momo', price=60, inventory=200)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True)
        client = APIClient()
        response = client.get('/restaurant/menu/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_data.data, response.data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/json')
