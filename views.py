# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

# Create your views here.
from rest_framework import generics
#from django.contrib.auth import Users
#todo: import users
from .serializers import QuestionSerializer
from .models import question


class QuestionSearchAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    #lookup_field            = 
    serializer_class        = QuestionSerializer
    
    def get_queryset(self):
        qs = question.objects.all()
        n_questions=self.request.GET.get("n_questions")
        question_type = self.request.GET.get("question_type")
        subject = self.request.GET.get("subject")
        difficulty = self.request.GET.get("difficulty")
        chapter=self.request.GET.get("chapter")
        standard=self.request.GET.get("standard")
        goal=self.request.GET.get("goal")
        stream=self.request.GET.get("stream")
        topic=self.request.GET.get("topic")
        subtopic=self.request.GET.get("subtopic")
        marks=self.request.GET.get("marks")
        exam_appearances=self.request.GET.get("exam_appearances")
        tags=self.request.GET.get("tags")


        if question_type is not None:
            qs = qs.filter(question_type__iexact=question_type)
        if difficulty is not None:
            qs = qs.filter(difficulty__iexact=difficulty)
        if subject is not None:
            qs = qs.filter(difficulty__iexact=subject)
        if chapter is not None:
            qs = qs.filter(chapter__iexact=chapter)
        if standard is not None:
            qs = qs.filter(standard__iexact=standard)
        if goal is not None:
            qs = qs.filter(goal__iexact=goal)
        if stream is not None:
            qs = qs.filter(stream__iexact=stream)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if subtopic is not None:
            qs = qs.filter(subtopic__iexact=subtopic)
        if marks is not None:
            qs = qs.filter(marks__iexact=marks)
        if exam_appearances is not None:
            qs = qs.filter(exam_appearances__gte=exam_appearances)
        if tags is not None:
            qs = qs.filter(tags__contains=tags)
        return qs

class QuestionTestAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    #lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = QuestionSerializer
    #queryset                = BlogPost.objects.all()

    def get_queryset(self):
        qs = question.objects.all()

        n_questions=self.request.GET.get("n_questions")
        question_type = self.request.GET.get("question_type")
        difficulty = self.request.GET.get("difficulty")
        subject = self.request.GET.get("subject")
        chapter=self.request.GET.get("chapter")
        standard=self.request.GET.get("standard")
        goal=self.request.GET.get("goal")
        stream=self.request.GET.get("stream")
        topic=self.request.GET.get("topic")
        subtopic=self.request.GET.get("subtopic")
        marks=self.request.GET.get("marks")

        # filter by the user for not correctly submitted user 
        user = self.request.user



        if question_type is not None:
            qs = qs.filter(question_type__iexact=question_type)
        if difficulty is not None:
            qs = qs.filter(difficulty__iexact=difficulty)
        if subject is not None:
            qs = qs.filter(subject__iexact=subject)
        if chapter is not None:
            qs = qs.filter(chapter__iexact=chapter)
        if standard is not None:
            qs = qs.filter(standard__iexact=standard)
        if goal is not None:
            qs = qs.filter(goal__iexact=goal)
        if stream is not None:
            qs = qs.filter(stream__iexact=stream)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if subtopic is not None:
            qs = qs.filter(subtopic__iexact=subtopic)
        if marks is not None:
            qs = qs.filter(marks__iexact=marks)
        return qs


class QuestionChallengeAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    #lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = QuestionSerializer
    #queryset                = BlogPost.objects.all()

    def get_queryset(self):
        qs = question.objects.all()
        question_type = self.request.GET.get("question_type")
        difficulty = self.request.GET.get("difficulty")
        subject = self.request.GET.get("subject")
        chapter=self.request.GET.get("chapter")
        standard=self.request.GET.get("standard")
        goal=self.request.GET.get("goal")
        stream=self.request.GET.get("stream")
        topic=self.request.GET.get("topic")
        subtopic=self.request.GET.get("subtopic")
        marks=self.request.GET.get("marks")

        #filter by both users for not done questions

        user1 = self.request.user
        user2=marks=self.request.GET.get("opponent")


        if question_type is not None:
            qs = qs.filter(question_type__iexact=question_type)
        if difficulty is not None:
            qs = qs.filter(difficulty__iexact=difficulty)
        if subject is not None:
            qs = qs.filter(subject__iexact=subject)
        if chapter is not None:
            qs = qs.filter(chapter__iexact=chapter)
        if standard is not None:
            qs = qs.filter(standard__iexact=standard)
        if goal is not None:
            qs = qs.filter(goal__iexact=goal)
        if stream is not None:
            qs = qs.filter(stream__iexact=stream)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if subtopic is not None:
            qs = qs.filter(subtopic__iexact=subtopic)
        if marks is not None:
            qs = qs.filter(marks__iexact=marks)
        return qs


