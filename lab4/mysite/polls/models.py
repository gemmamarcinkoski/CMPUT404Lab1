from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
#defining stuff we want to store on our dtabase

@python_2_unicode_compatible
class Question(models.Model): #this si going to be a table
	question_text = models.CharField(max_length=200)#this is goign to be a column/field in the question table
	pub_date = models.DateTimeField('date published') 
	def __str__(self):
		#so that python returns data neatly
		return self.question_text
	def was_published_recently(self):
#we want this to return tue if the question was published in the last day
		now = timezone.now()
		return now -  datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

