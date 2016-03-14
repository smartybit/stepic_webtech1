from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    raiting = models.IntegerField()
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    likes= models.ForeignKey(User, on_delete = models.SET_NULL)
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question models.ForeignKey(Question, on_delete = models.CASCADE)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
	
