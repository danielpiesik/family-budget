from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from .models import User


class UsersTests(TestCase):
    fixtures = ['users']

    def test_successful_user_creating(self):
        body = {
            'username': 'new-user',
            'password': 'pass',
        }
        url = reverse('users-list')

        self.assertFalse(User.objects.filter(username='new-user').exists())

        response = self.client.post(url, body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='new-user').exists())

        user = User.objects.get(username='new-user')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_user_already_exists(self):
        user = User.objects.first()
        body = {
            'username': user.username,
            'password': 'some-password',
        }
        url = reverse('users-list')

        response = self.client.post(url, body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            response.json(),
            {'username': ['A user with that username already exists.']},
        )
