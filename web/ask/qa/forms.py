from django import forms
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

#form = AnswerForm(initial={'question_id': question_id})
