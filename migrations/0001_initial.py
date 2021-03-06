# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 19:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('chapter', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'classcast_chapter_index',
            },
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('xblock_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('question_type', models.CharField(max_length=50)),
                ('standard', models.IntegerField()),
                ('stream', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('goal', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField(default=0)),
                ('chapter', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('subtopic', models.CharField(max_length=100)),
                ('question_image', models.CharField(blank=True, max_length=100)),
                ('option1_image', models.CharField(blank=True, max_length=100)),
                ('option2_image', models.CharField(blank=True, max_length=100)),
                ('option3_image', models.CharField(blank=True, max_length=100)),
                ('option4_image', models.CharField(blank=True, max_length=100)),
                ('num_correct_submissions', models.IntegerField(default=0)),
                ('average_time_to_answer', models.FloatField(default=0.0)),
                ('tags', models.CharField(max_length=100, null=True)),
                ('exam_appearances', models.IntegerField(default=0)),
                ('num_deliveries', models.IntegerField(default=0)),
                ('num_skipped', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'classcast_questions',
            },
        ),
        migrations.CreateModel(
            name='student_topic_interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.IntegerField(default=0)),
                ('num_attempts', models.IntegerField(default=0)),
                ('num_skipped', models.IntegerField(default=0)),
                ('num_corrects', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'classcast_student_topic_interaction',
            },
        ),
        migrations.CreateModel(
            name='topics',
            fields=[
                ('topic_name', models.CharField(max_length=255)),
                ('topic_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classcast_search_fetch.chapter')),
            ],
            options={
                'db_table': 'classcast_topic_index',
            },
        ),
        migrations.AddField(
            model_name='student_topic_interaction',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classcast_search_fetch.topics'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('standard', 'subject', 'chapter')]),
        ),
        migrations.AlterUniqueTogether(
            name='student_topic_interaction',
            unique_together=set([('student', 'topic', 'difficulty')]),
        ),
    ]
