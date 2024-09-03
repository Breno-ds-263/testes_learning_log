from django.test import TestCase
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry

class XSSProtectionTest(TestCase):
    def setUp(self):
        # Configura usuário, tópico e entrada
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.topic = Topic.objects.create(owner=self.user, text='Test Topic')
        self.entry = Entry.objects.create(topic=self.topic, text='Initial Text')

    def test_xss_protection_in_entry_edit(self):
        # Tenta inserir código malicioso na entrada
        malicious_script = '<script>alert("XSS")</script>'
        response = self.client.post(reverse('learning_logs:edit_entry', args=[self.entry.id]), {
            'text': malicious_script,
            'topic': self.topic.id,
        })
        # Verifica se o script foi neutralizado (escapado)
        self.assertNotContains(response, malicious_script, html=True)
