# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import permissions

from quizshowdown.core import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    model = models.Quiz
    serializer_class = serializers.QuizSerializer

    def pre_save(self, obj):
        print 'aaaaaaaaaaaa'
        obj.commited_by = self.request.user


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
