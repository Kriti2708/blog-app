from django import forms
from .models import Post, Comment, Profile
# from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'author']
        widgets = {'author': forms.HiddenInput()}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'body', 'post']
        widgets = {
            'user': forms.HiddenInput(),
            'post': forms.HiddenInput()
            }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'picture', 'bio']
        widgets = {
            'user': forms.HiddenInput(),
            }
