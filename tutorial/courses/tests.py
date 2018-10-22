# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.






class CourseModelTest(TestCase):
	def create_category(name='sam', imgpath='https'):
		return Category.objects.create(name=name, imgpath=imgpath)

	def test_create_category(self):
		category = self.create_category()
		self.assertEqual(category.__str__(), category.name)
		self.assertTrue(isinstance(category, Category))

	def create_course(self):
		course = Course.objects.create(
				name='nam',
				description='des',
				logo='logo',
				category=create_category()
			)
		return course

	

	def course_id(self):
		id1 = self.create_course()
		id1.contacts.create(
			type='PHONE',
			value='228322'
		)
		id1.branches.create(
			latitude='123',
			longtitude='321',
			address='111'
		)
		self.assertTrue(isinstance(id1, Course))
