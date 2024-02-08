from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'nombre': 'John Doe', 'cedula': '123456789', 'celular': '555-555-5555'}
        self.user = User.objects.create(**self.user_data)

    def test_get_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], self.user_data['nombre'])
