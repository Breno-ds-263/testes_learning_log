from django.test import TestCase
from django.urls import reverse

class LoginRequiredTest(TestCase):
    def test_login_required_for_views(self):
        views = [
            reverse('learning_logs:topics'),
            reverse('learning_logs:topic', args=[1]),
            reverse('learning_logs:new_topic'),
            reverse('learning_logs:new_entry', args=[1]),
            reverse('learning_logs:edit_entry', args=[1]),
        ]
        for view in views:
            response = self.client.get(view)
            self.assertRedirects(response, f'/accounts/login/?next={view}')
