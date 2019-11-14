from django.test import TestCase
from projects.views import project_index
from django.urls import reverse

class TestViews(TestCase):

	def test_project_index_request(self):		
		response = project_index(reverse('project_index'))
		self.assertEqual(response.status_code, 200)
