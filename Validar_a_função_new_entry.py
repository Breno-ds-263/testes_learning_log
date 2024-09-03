from django.test import TestCase
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry

class NewEntryValidationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_new_entry_without_topic(self):
        response = self.client.post(reverse('learning_logs:new_entry', args=[None]), {'text': 'Test Entry'})
        self.assertEqual(response.status_code, 400)  # Assuming the backend returns 400 for bad request


class EditEntryProtectionTest(TestCase):
    def setUp(self):
        # Configura dois usuários, um tópico e uma entrada
        self.user1 = User.objects.create_user(username='user1', password='12345')
        self.user2 = User.objects.create_user(username='user2', password='12345')
        self.topic = Topic.objects.create(owner=self.user1, text='User1 Topic')
        self.entry = Entry.objects.create(topic=self.topic, text='User1 Entry')

    def test_edit_entry_without_permission(self):
        self.client.login(username='user2', password='12345')
        response = self.client.post(reverse('learning_logs:edit_entry', args=[self.entry.id]), {
            'text': 'Malicious Edit',
            'topic': self.topic.id,
        })
        self.assertEqual(response.status_code, 404)
