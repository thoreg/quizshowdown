from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Quiz(models.Model):
    question = models.CharField(max_length=255)
    solution = models.PositiveSmallIntegerField()
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    catetory = models.ForeignKey(Category)
    # commited_by = models.ForeignKey(User)
