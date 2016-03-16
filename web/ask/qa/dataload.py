from django.db import models
from django.contrib.auth.models import User
from models import Question, User, Answer
from datetime import datetime
import  random as random

def createdata():
    users = []
    for i in range(3):
        user, created = User.objects.get_or_create(username='test' + repr(i))
        if created:
            user.password = 'test'
            user.save()
        users += [user]

    
    questions = []
    for i in range(3):
        numstr = repr(i)
        question = Question(title='Question #' + numstr, text = 'Question text #' + numstr, author = user)
        question.added_at = datetime.now()
        question.raiting = 10 - i
        question.save()
        questions += [question]

    for i in range(10):
        answer = Answer(author = random.choice(users), text = 'Answer #' + repr(i), question = random.choice(questions))
        answer.added_at = datetime.now()
        answer.save()
    return None         
