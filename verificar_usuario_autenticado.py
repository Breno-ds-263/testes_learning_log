from django.test import TestCase
from django.urls import reverse

class EntryAccessTest(TestCase):
    def test_access_entry_without_authentication(self):
        # Tentativa de acessar uma URL de leitura sem estar logado
        response = self.client.get(reverse('learning_logs:entry', args=[1]))
        # Verifica se redireciona para a página de login
        self.assertRedirects(response, '/accounts/login/?next=/entry/1/')
