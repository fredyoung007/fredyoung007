from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Quiz model
class Quiz(models.Model):
    name = models.CharField(max_length=200, default="name")
    description = models.TextField()

    def __str__(self):
        return f'title={self.name} content={self.description}' 

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField()
    score = models.IntegerField(default=0)

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False

    def __str__(self):
        return f'question={self.question } score={self.score} quiz={self.quiz_id}'

class Choice(models.Model):
    choice = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f'ID={self.id} order= {self.order} choice={self.choice} qeustion={self.question_id} is_correct={self.is_correct} rate={self.rate}'

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        cstr = ','.join(str(c) for c in self.choices.all())
        return f'Submission: ID={self.id}; choices=[{cstr}]'
