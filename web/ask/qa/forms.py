from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import models as models

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) == 0:
            raise forms.ValidationError("Title must not be empty")
        return title
            
        
    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if len(text) == 0:
            raise forms.ValidationError("Question text must not be empty")
        return text

    def save(self):
        question = models.Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question.id

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.CharField(widget=forms.HiddenInput())

    def get_question_id(self):
        return self.cleaned_data['question_id']
       
    
    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if len(text) == 0:
            raise forms.ValidationError("Question text must not be empty")
        return text

    def save(self):
        answer = models.Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return self.cleaned_data['question_id']

class SignupForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email")

#    def clean_username(self):
#        theuser = super(UserCreationForm, self).save(commit=False)
#        username = theuser.username
#        raise username
#        username = username.strip()
#        if 
#        if  User.objects.filter(username__iexact=username).first() != None:
#            raise forms.ValidationError("This login is already in use")
#        return username

    def clean_email(self):
#        email = super(UserCreationForm, self).clean_email()
        #user = super(UserCreationForm, self).save(commit=False)
        ce = self.cleaned_data
        email = self.cleaned_data["email"] 
        if  User.objects.filter(email__iexact=email).first() != None:
            raise forms.ValidationError("This email is already in use ;-)")
        return email

    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
