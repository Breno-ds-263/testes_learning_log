from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from time import sleep

class RateLimitingTest(TestCase):
    def setUp(self):
        # Configura usuário de teste
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_rate_limiting_on_login(self):
        login_url = reverse('login')
        for i in range(5):  # Simula múltiplas tentativas falhas de login
            response = self.client.post(login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        
        # Verifica se a tentativa de login é bloqueada após múltiplas falhas
        response = self.client.post(login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 429)
