from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from learning_logs.models import Topic

class TopicAccessTest(TestCase):
    def setUp(self):
        # Configura dois usuários e um tópico
        self.user1 = User.objects.create_user(username='user1', password='12345')
        self.user2 = User.objects.create_user(username='user2', password='12345')
        self.topic = Topic.objects.create(owner=self.user1, text='User1 Topic')

    def test_access_topic_without_permission(self):
        self.client.login(username='user2', password='12345')
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 404)
