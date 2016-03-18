from django import forms
import models as models

class QuestionForm(forms.Form):
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


#form = AnswerForm(initial={'question': question_id})
