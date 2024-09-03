from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class NewTopicRedirectionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_new_topic_redirection(self):
        response = self.client.post(reverse('learning_logs:new_topic'), {'text': 'New Topic'})
        self.assertRedirects(response, reverse('learning_logs:topics'))
