from django.test import TestCase
from django.urls import reverse

class PageLoadTest(TestCase):
    def test_main_page_loads(self):
        response = self.client.get(reverse('learning_logs:index'))
        self.assertEqual(response.status_code, 200)

class SystemOverloadTest(TestCase):
    def make_request(self):
        return self.client.get(reverse('learning_logs:index'))

    def test_system_overload(self):
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = list(executor.map(self.make_request, range(1000)))

        # A ideia seria verificar se algum request retornou 503 Service Unavailable
        for response in results:
            self.assertNotEqual(response.status_code, 503)
