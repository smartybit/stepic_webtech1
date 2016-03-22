from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import models as models

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    user = User()

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
        if not self.user.is_authenticated():
            raise Exception('User not authenticated')
        question.author = self.user
        question.save()
        return question.id

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.CharField(widget=forms.HiddenInput())
    user = User()
    def get_question_id(self):
        return self.cleaned_data['question_id']
       
    
    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if len(text) == 0:
            raise forms.ValidationError("Question text must not be empty")
        return text

    def save(self):
        answer = models.Answer(**self.cleaned_data)
        if not self.user.is_authenticated():
            raise Exception('User not authenticated')
        answer.author = self.user
        answer.save()
        return self.cleaned_data['question_id']

class SignupForm(UserCreationForm):

    FIELD_NAME_MAPPING = {'password1': 'password', }

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs["id"] = "password"
        self.fields['password2'].blank = True
        self.fields['password2'].required= False

    def add_prefix(self, field_name):
        field_name = self.FIELD_NAME_MAPPING.get(field_name, field_name)
        return super(UserCreationForm, self).add_prefix(field_name)

    def clean_password2(self):
        return self.cleaned_data.get("password1")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            raise forms.ValidationError("Email is required!")

        if  User.objects.filter(email__iexact=email).first() != None:
            raise forms.ValidationError("This email is already in use ;-)")
        return email

    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
