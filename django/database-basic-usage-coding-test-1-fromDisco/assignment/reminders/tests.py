from django.test import TestCase
from django.urls import reverse
from django.shortcuts import resolve_url

from .models import Reminder

class MathTest(TestCase):
    def test_addition_operation(self):
        url = reverse('math')
        response = self.client.get(f"{url}?operation=add&a=1&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

class DeleteReminderTest(TestCase):
    def test_delete_reminder(self):
        instance = Reminder.objects.create(title="TEST", description="the delete function")

        url = f'/reminders/{instance.id}/delete'
        response = self.client.delete(f"{url}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"message": "Successfully deleted"}')

