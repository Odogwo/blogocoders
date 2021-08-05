from django.db import models

# Create your models here.

class Book(models.Model):
	book_title = models.CharField(max_length=150)
	publication_year = models.IntegerField()
	author = models.CharField(max_length=100)
	plot = models.TextField()
	

	def __str__(self):
		return self.book_title