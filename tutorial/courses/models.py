from django.db import models


form = (
	('email','EMAIL'),
	('fb','FACEBOOK'),
	('phone','PHONE'),
)


class Course(models.Model):
	category = models.CharField(max_length=100)
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
	branch = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')



class Contact(models.Model):
	type = models.CharField(choices=form, max_length=10, default='PHONE')
	value = models.CharField(max_length=100)
	contact = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
	def __str__(self):
		return self.type