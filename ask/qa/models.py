from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class MyUser(User):
    def __str__(self):
        return self.username

class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')

    def popular(self):
        return Question.objects.order_by('-rating')

class Question(models.Model):
    manager = QuestionManager()
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.CharField(max_length=64)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.text
