from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "slug", "banner"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "banner": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
