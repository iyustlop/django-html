from django.test import TestCase
from django.urls import reverse
from .models import Worker

# Create your tests here.

class WorkerNameViewTest(TestCase):
    def test_worker_name_view(self):
        # Create a Worker instance
        worker = Worker.objects.create(name='Test Worker', email='test@example.com', location='Test Location')

        # Get the URL for the worker_name view
        url = reverse('worker_name', args=[worker.name])

        # Make a request to the URL
        response = self.client.get(url)

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct worker is in the context
        self.assertEqual(response.context['worker'].name, 'Test Worker')

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'worker.html')
