from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from short_link_user.models import ShortedLink


class LinkResolverTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.original_link = reverse('login')
        self.shortedLink = 'qqqq'
        shorted_link_object = ShortedLink(
            orig_url=self.original_link,
            short_url=self.shortedLink,
            creator=user
        )
        shorted_link_object.save()

    def test_resolve_link(self):
        response = self.client.get(reverse('resolve-link', kwargs={'identifier': self.shortedLink}), follow=True)
        self.assertRedirects(response, self.original_link)


# test link generation
class LinkGeneratorTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.user = user
        self.client.login(username='testuser', password='12345')

    def test_link_generator(self):
        link = b'/MQ'
        data = {
            'link': '/',
            'user': self.user.id
        }
        response = self.client.post(reverse('generate-link'), data, follow=True)
        self.assertEqual(response.content, link)
