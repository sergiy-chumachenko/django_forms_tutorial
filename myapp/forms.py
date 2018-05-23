from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'body')
