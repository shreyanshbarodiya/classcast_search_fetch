# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class question(models.Model):
	xblock_id= models.CharField(max_length=1000, primary_key=True)
	question_type=models.CharField(max_length=50)
	standard=models.IntegerField()
	stream=models.CharField(max_length=100)
	subject=models.CharField(max_length=50)
	marks=models.IntegerField()
	goal=models.CharField(max_length=100)
	difficulty=models.IntegerField(default=0)
	chapter=models.CharField(max_length=100)
	topic=models.CharField(max_length=100)
	subtopic=models.CharField(max_length=100)
	question_image=models.CharField(max_length=100,blank=True)
	option1_image=models.CharField(max_length=100,blank=True)
	option2_image=models.CharField(max_length=100,blank=True)
	option3_image=models.CharField(max_length=100,blank=True)
	option4_image=models.CharField(max_length=100,blank=True)
	num_correct_submissions=models.IntegerField(default=0)
	average_time_to_answer=models.FloatField(default=0.0)
	tags=models.CharField(max_length=100,null=True)
	exam_appearances=models.IntegerField(default=0)
	num_deliveries=models.IntegerField(default=0)
	num_skipped=models.IntegerField(default=0)

	class Meta:
		db_table = 'classcast_questions'

	def __str__(self):
		return u'%s %s %s' % (str(self.subject), str(self.topic), str(self.xblock_id))

class chapter(models.Model):
	standard =models.IntegerField(primary_key=True)
	subject=models.CharField(max_length=50, primary_key=True)
	chapter=models.CharField(max_length=255, primary_key=True)

	class Meta:
		db_table = 'classcast_chapter_index'

	def __str__(self):
		return str(self.standard) + ":" + self.subject + ":" + self.chapter 

class topics(models.Model):
	standard =models.IntegerField()
	subject=models.CharField(max_length=50)
	chapter=models.CharField(max_length=255)	
	topic_name=models.CharField(max_length=255)
	topic_id=models.IntegerField(primary_key=True)

	class Meta:
		db_table = 'classcast_topic_index'

	def __str__(self):
		return str(self.standard) + ":" + self.subject + ":" + self.chapter + ":" + self.topic_name

class student_topic_interaction(models.Model):
	student_id= models.IntegerField(primary_key=True)
	topic_id=models.IntegerField(primary_key=True)
	difficulty=models.IntegerField(primary_key=True)
	num_attempts=models.IntegerField(default=0)
	num_skipped=models.IntegerField(default=0)
	num_corrects=models.IntegerField(default=0)

	class Meta:
		db_table = 'classcast_student_topic_interaction'

	def __str__(self):
		return self.student_id + ":" + self.topic_id

