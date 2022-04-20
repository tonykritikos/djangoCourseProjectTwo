from django import forms
from django.forms import models

from .models import Comment


class CommentForm(models.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "texr": "Your comment"
        }
