# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

# Create your views here.
from rest_framework import generics
from .serializers import QuestionSerializer
from .models import question,student_topic_interaction,topics
#todo:from appname.models import test_submissions
#import submisson here 
from django.db.models import Q
import random
from itertools import chain

from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import InvalidLocationError, ItemNotFoundError
# from opaque_keys.edx.keys import UsageKey
# import cms.djangoapps.contentstore.views as cdcv
# import cms.djangoapps.contentstore as cdc
# from cms.djangoapps.contentstore.item import classcast_xblock_data


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

        # from cms.djangoapps.contentstore.views.item import classcast_xblock_data
        # import cms.djangoapps.contentstore.utils

        for que in qs:
            que.data = _xblock_data(que.xblock_id, self.request.user)

        return qs

class QuestionTestAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    serializer_class        = QuestionSerializer

    def get_queryset(self):
        qs = question.objects.all()

        #n_questions=self.request.GET.get("n_questions")
        question_type = self.request.GET.get("question_type")
        # difficulty = self.request.GET.get("difficulty")
        subject = self.request.GET.get("subject")
        #chapter=self.request.GET.get("chapter")
        chapter=request.GET.getlist('chapter')
        standard=self.request.GET.get("standard")
        goal=self.request.GET.get("goal")
        stream=self.request.GET.get("stream")
        topic=self.request.GET.get("topic")
        subtopic=self.request.GET.get("subtopic")
        marks=self.request.GET.get("marks")

        duration=int(self.request.GET.get("duration"))
        if duration==30 :
            n_questions=12
        elif duration==60:
            n_questions=24
        else:
            n_questions=10


        # filter by the user for not correctly submitted user 
        # user_id = self.request.user.id
        # submissions=test_submissions.objects.all().filter(student_id=user_id)
        # submissions=submissions.filter(Q(correctly_attempted_in_test__gte=1) |Q(correctly_attempted_in_gym__gte=1)).values('xblock_id')



        if goal is not None:
            qs = qs.filter(goal__iexact=goal)
        if stream is not None:
            qs = qs.filter(stream__iexact=stream)
        if standard is not None:
            qs = qs.filter(standard__iexact=standard)
        if subject is not None:
            qs = qs.filter(subject__iexact=subject)
        if chapter is not None:
            qs = qs.filter(chapter__in=chapter)
        if question_type is not None:
            qs = qs.filter(question_type__iexact=question_type)
        # if difficulty is not None:
        #     qs = qs.filter(difficulty__iexact=difficulty)
        if topic is not None:
            qs = qs.filter(topic__iexact=topic)
        if subtopic is not None:
            qs = qs.filter(subtopic__iexact=subtopic)
        if marks is not None:
            qs = qs.filter(marks__iexact=marks)

        #qs.exclude(xblock_id__in=submissions)
        #TODO: add condition if number of total questions in difficulty d is less than n_questions/3 
        qs0=qs.filter(difficulty=0).order_by('?')[:(n_questions/3)]
        qs1=qs.filter(difficulty=1).order_by('?')[:(n_questions/3)]
        qs2=qs.filter(difficulty=2).order_by('?')[:(n_questions/3)]
        # qs0.union(qs1, qs2)
        # return qs0 | qs1 | qs2
        qs_final = list(chain(qs0, qs1, qs2))
        return qs_final

class QuestionChallengeAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    serializer_class        = QuestionSerializer

    def get_queryset(self):
        qs = question.objects.all()
        question_type = self.request.GET.get("question_type")
        difficulty = self.request.GET.get("difficulty")
        subject = self.request.GET.get("subject")
        #chapter=self.request.GET.get("chapter")
        chapter=request.GET.getlist('chapter')
        standard=self.request.GET.get("standard")
        goal=self.request.GET.get("goal")
        stream=self.request.GET.get("stream")
        topic=self.request.GET.get("topic")
        subtopic=self.request.GET.get("subtopic")
        marks=self.request.GET.get("marks")
        n_questions=self.request.GET.get("n_questions")
        #filter by both users for not done questions
        #WHY user2_id=marks???
        # user1_id = self.request.user.id
        # user2_id=marks=self.request.GET.get("opponent")
        # submissions1=test_submissions.objects.all().filter(student_id=user1_id)
        # submissions1=submissions1.filter(Q(correctly_attempted_in_test__gte=1) |Q(correctly_attempted_in_gym__gte=1)).values('xblock_id')
        # submissions2=test_submissions.objects.all().filter(student_id=user2_id)
        # submissions2=submissions2.filter(Q(correctly_attempted_in_test__gte=1) |Q(correctly_attempted_in_gym__gte=1)).values('xblock_id')



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
        if subtopic is not None:
            qs = qs.filter(subtopic__iexact=subtopic)
        if marks is not None:
            qs = qs.filter(marks__iexact=marks)

        qs.order_by('?')[:n_questions]
        return qs


class QuestionGymAPIView(generics.ListAPIView): # DetailView CreateView FormView
    #queryset = question.objects.all()
    serializer_class        = QuestionSerializer

    def get_queryset(self):
        qs = question.objects.all()
        topic_list = topics.objects.all()

        n_questions=3 # fetch questions in the batches of 3
        correct_threshold=3
        subject = self.request.GET.get("subject")
        chapter=self.request.GET.get("chapter")
        standard=self.request.GET.get("standard")


        # filter by the user for not correctly submitted user 
        student_id = self.request.user.id

        
        if standard is not None:
            qs = qs.filter(standard__iexact=standard)
            topic_list = topic_list.filter(standard__iexact=standard)
        if subject is not None:
            qs = qs.filter(subject__iexact=subject)
            topic_list = topic_list.filter(subject__iexact=subject)
        if chapter is not None:
            qs = qs.filter(chapter__iexact=chapter)
            topic_list = topic_list.filter(chapter__iexact=chapter)
        
        #fetch topic list of given chapter
        # topic_list=topics.objects.all().filter(standard__iexact=standard, subject__iexact=subject, chapter__iexact=chapter)
        fetch_topic=''
        fetch_difficulty=''
        #iterate over topics and look for current topic and difficulty of user
        for topic in topic_list.iterator():
            submissions_easy=student_topic_interaction.objects.filter(student_id=student_id,difficulty=0, topic_id=topic.topic_id).first()
            submissions_medium=student_topic_interaction.objects.filter(student_id=student_id,difficulty=1, topic_id=topic.topic_id).first()
            submissions_difficult=student_topic_interaction.objects.filter(student_id=student_id,difficulty=2, topic_id=topic.topic_id).first()
            #if number of diffiuclt correct question greater than threshold go to next topic
            if submissions_difficult is not None and submissions_difficult.values('num_corrects')>=correct_threshold:
                continue;
            #if number of mediumm correct question greater than threshold choose current topic and diffuclt level
            elif submissions_medium is not None and submissions_medium.values('num_corrects') >=correct_threshold:
                fetch_difficulty=2
                fetch_topic=topic
                break
            elif submissions_easy is not None and submissions_easy.values('num_corrects') >=correct_threshold:
                fetch_difficulty=1
                fetch_topic=topic
                break
            else :
                fetch_difficulty=0
                fetch_topic=topic
                break

        # fetch 3 questions of fetch_difficulty and fetch topic
        #if done on all topics do something here , currently 
        #using a random topic and random diffiuclty 
        if fetch_topic=='':
            fetch_topic=random.choice(topic_list)
            fetch_difficulty=random.choice([0,1,2])        

        qs = qs.filter(topic__iexact=fetch_topic.topic_name)
        qs=qs.filter(difficulty=fetch_difficulty).order_by('?')[:(n_questions)]
        return qs

def _xblock_data(xblock_id, user):
    usage_key = usage_key_with_run(xblock_id)

    with modulestore().bulk_operations(usage_key.course_key):
        response = _get_xblock(usage_key, user)
    
    if(response is None):
        return "Invalid Question ID"
    
    data = getattr(response, 'data', '')
    return data



def _get_xblock(usage_key, user):
    """
    Returns the xblock for the specified usage key. Note: if failing to find a key with a category
    in the CREATE_IF_NOT_FOUND list, an xblock will be created and saved automatically.
    """

    store = modulestore()
    with store.bulk_operations(usage_key.course_key):
        try:
            return store.get_item(usage_key, depth=None)
        except ItemNotFoundError:
            return None
        except InvalidLocationError:
            return None