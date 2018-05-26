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
	difficulty=models.CharField(max_length=100)
	chapter=models.CharField(max_length=100)
	topic=models.CharField(max_length=100)
	subtopic=models.CharField(max_length=100)
	question_image=models.CharField(max_length=100,blank=True)
	option1_image=models.CharField(max_length=100,blank=True)
	option2_image=models.CharField(max_length=100,blank=True)
	option3_image=models.CharField(max_length=100,blank=True)
	option4_image=models.CharField(max_length=100,blank=True)
	num_correct_submissions=models.IntegerField()
	average_time_to_answer=models.FloatField()
	tags=models.CharField(max_length=100,null=True)
	exam_appearances=models.IntegerField()
	num_deliveries=models.IntegerField()
	num_skipped=models.IntegerField()

	class Meta:
		db_table = 'classcast_questions'

	def __str__(self):
		return u'%s %s %s' % (str(self.subject), str(self.topic), str(self.xblock_id))

class chapter(models.Model):
	standard =models.IntegerField()
	subject=models.CharField(max_length=50)
	chapter=models.CharField(max_length=255)


	def __str__(self):
		return self.chapter_name

class topics(models.Model):
	chapter_name=models.ForeignKey(chapter, on_delete=models.CASCADE)
	topic=models.CharField(max_length=255)

	def __str__(self):
		return chapter_name+ ":" + topic_name

class student_topic_interaction(models.Model):
	student_id= models.ForeignKey()
	topic=models.ForeignKey(topics)
	difficulty=models.IntegerField()
	num_attempts=models.IntegerField()
	num_skipped=models.IntegerField()
	num_corrects=models.IntegerField()


	def __str__(self):
		return student_id+":"+topic
