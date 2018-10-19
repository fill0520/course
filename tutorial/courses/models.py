from django.db import models


form = (
	('EMAIL','EMAIL'),
	('FACEBOOK','FACEBOOK'),
	('PHONE','PHONE'),
)

class Category(models.Model):
	name = models.CharField(max_length=100)
	imgpath = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class Course(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	logo = models.CharField(max_length=100)
	id = models.AutoField(primary_key=True)
	def __str__(self):
		return self.name

class Branch(models.Model):
	latitude = models.CharField(max_length=100)
	longtitude = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')



class Contact(models.Model):
	type = models.CharField(choices=form, max_length=10, default='PHONE')
	value = models.CharField(max_length=100)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
	def __str__(self):
		return self.type