# -*- coding: utf-8 -*-
from rest_framework import serializers

from quizshowdown.core import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ('id', 'question', 'category')
        exclude = ('commited_by', )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'text', 'quiz', 'is_solution')
