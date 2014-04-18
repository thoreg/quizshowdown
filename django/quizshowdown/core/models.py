# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name


class Answer(models.Model):
    text = models.CharField(max_length=50)
    quiz = models.ForeignKey('Quiz')
    is_solution = models.BooleanField()


class UserProfile(User):
    highscore = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Quiz(models.Model):
    question = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    commited_by = models.ForeignKey(UserProfile)
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.question
