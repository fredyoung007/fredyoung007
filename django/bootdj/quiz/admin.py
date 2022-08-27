from django.contrib import admin
from .models import Quiz, Question, Choice, Submission

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['name']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice']

# Register 
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission)

