# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Answer(models.Model):
    text = models.CharField(max_length=50)
    quiz = models.ForeignKey('Quiz')
    is_solution = models.BooleanField()


class Quiz(models.Model):
    question = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    commited_by = models.ForeignKey(User)
