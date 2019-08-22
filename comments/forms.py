from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'TITLE'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'COMMENT'}))
    class Meta:
        model = Comment
        fields = ['comment']