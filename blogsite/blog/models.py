from django.db import models
from django.db import models
from django.utils.timezone import now
from django.contrib import admin
# Create your models here.


class BlogPostAdmin(model.Model): 
	search_fields = ['Title', 'Subtitle', 'Content', 'Date', 'Autor', "Category1", "Category2", "Category3",
	"Tag1", "Tag2", "Tag3", "Tag4", "Tag5", "Tag6", "Tag7", "Tag8", "Tag9", "Tag10" ]

class BlogPost(models.Model):
	title = models.CharField('Title', max_length=255)
	subtitle = models.CharField('Subtitle', max_length=255)
	content = models.TextField('Content',  blank=False)
	date_published = models.DateTimeField('Date', default=now,  editable=True)
	author = models.CharField('Autor',max_length=255)
	catergory1 = models.CharField("Category1", max_length=255, blank=True)
	catergory2 = models.CharField("Category2", max_length=255, blank=True)
	catergory3 = models.CharField("Category3", max_length=255, blank=True)
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
