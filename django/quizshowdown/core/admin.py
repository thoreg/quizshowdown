from django.contrib import admin
from quizshowdown.core.models import Answer, Category, Quiz, UserProfile


class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = "quiz"


class QuizAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(UserProfile)
