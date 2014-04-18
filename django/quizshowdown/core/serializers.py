# -*- coding: utf-8 -*-
from rest_framework import serializers

from quizshowdown.core import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'text', 'quiz', 'is_solution')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ('id', 'question', 'category')
        exclude = ('commited_by', )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id',
                  'highscore',
                  'username',
                  'first_name',
                  'last_name',
                  'last_login',
                  'date_joined')
