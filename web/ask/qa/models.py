from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=False, auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "asked_questions",)
    likes= models.ManyToManyField(User, related_name = "liked _questions")
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        db_table = 'questions'
        ordering  = ['-added_at']
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = 'answers'
        ordering  = ['-added_at']
	
