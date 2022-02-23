from dataclasses import field
from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', ]
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentReplayForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class PostSearchForm(forms.Form):
    search = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
