from django.db import models
from django.db import models
from django.utils.timezone import now
from django.contrib import admin
# Create your models here.


class BlogPostAdmin(models.Model): 
	search_fields = ['Title', 'Subtitle', 'Content', 'Date', 'Autor', "Category1", "Category2", "Category3",
	"Tag1", "Tag2", "Tag3", "Tag4", "Tag5", "Tag6", "Tag7", "Tag8", "Tag9", "Tag10", 'read_count']

class BlogPost(models.Model):
	title = models.CharField('Title', max_length=255)
	subtitle = models.CharField('Subtitle', max_length=255, blank=True)
	content = models.TextField('Content1', blank=False)
	content2 = models.TextField('Content2', blank=True)
	date_published = models.DateTimeField('Date', default=now, editable=True)
	author = models.CharField('Autor',max_length=255)
	quotes = models.CharField('Quatation', max_length=255, blank=True)
	category1 = models.CharField("Category1", max_length=255, blank=True)
	category2 = models.CharField("Category2", max_length=255, blank=True)
	category3 = models.CharField("Category3", max_length=255, blank=True)
	tag1 = models.CharField("Tag1", max_length=255, blank=True)
	tag2 = models.CharField("Tag2", max_length=255, blank=True)
	tag3 = models.CharField("Tag3", max_length=255, blank=True)
	tag4 = models.CharField("Tag4", max_length=255, blank=True)
	tag5 = models.CharField("Tag5", max_length=255, blank=True)
	tag6 = models.CharField("Tag6", max_length=255, blank=True)
	tag7 = models.CharField("Tag7", max_length=255, blank=True)
	tag8 = models.CharField("Tag8", max_length=255, blank=True)
	tag9 = models.CharField("Tag9", max_length=255, blank=True)
	tag10 = models.CharField("Tag10", max_length=255, blank=True)
	read_count = models.IntegerField('Read Count', default=0)
	picture_name = models.CharField('Picture_name', max_length=255, blank=True)

	def __str__(self):
		return self.title
