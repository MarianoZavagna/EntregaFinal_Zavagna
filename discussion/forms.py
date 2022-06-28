from django import forms
from discussion.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model : Discussion
        fields = ['title', 'description', 'image']

