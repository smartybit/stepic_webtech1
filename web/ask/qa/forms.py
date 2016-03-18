from django import forms

class QuestionForm(forms.Form)
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean_title(self):
        self.title = self.title.strip()
        if len(self.title) = 0:
            raise forms.ValidationError("Title must not be empty")
            
        
    def clean_text(self):
        self.text = self.text.strip()
        if len(self.text) = 0:
            raise forms.ValidationError("Question text must not be empty")


#form = AnswerForm(initial={'question': question_id})
