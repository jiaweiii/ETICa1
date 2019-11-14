from django.test import TestCase
from blog.views import blog_index
from blog.views import blog_detail
from blog.views import blog_category
from django.urls import reverse
from blog.models import Category, Post, Comment
import pytest

class TestViews(TestCase):

	def test_blog_index_request(self):		
		response = blog_index(reverse('blog_index'))
		self.assertEqual(response.status_code, 200)
		
	#def test_blog_category_request(self):		
	#	response = blog_category(reverse('blog_category'))
	#	self.assertEqual(response.status_code, 200)
		
	def test_blog_detail_request(self):
		response = blog_detail(reverse('blog_detail'))
		self.assertEqual(response.status_code, 200)