from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserCreateTestCase(TestCase):
    def test_user_create(self):
        data = {
            'username': 'testUser2',
            'email': 'testEmail@example.com',
            'password1': 'lkjhgfdsa099',
            'password2': 'lkjhgfdsa099'
        }
        response = self.client.post(reverse('register'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        users = User.objects.all()
        self.assertEqual(users.count(), 1)


class UserLoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_user_login(self):
        credentials = {
            'username': 'testuser',
            'password': '12345'}
        response = self.client.post(reverse('login'), credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_user_login_wrong_password(self):
        credentials = {
            'username': 'testuser',
            'password': '1234'}
        response = self.client.post(reverse('login'), credentials, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_user_login_wrong_username(self):
        credentials = {
            'username': 'test',
            'password': '12345'}
        response = self.client.post(reverse('login'), credentials, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)


class UserShortedLinksTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_unauthorized_user(self):
        response = self.client.get(reverse('user_shorted_links'))
        self.assertEqual(response.status_code, 404)

    def test_authorized_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_shorted_links'))
        self.assertEqual(response.status_code, 200)