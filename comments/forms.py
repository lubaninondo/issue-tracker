from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'COMMENT'}))
    class Meta:
        model = Comment
        fields = ['comment']