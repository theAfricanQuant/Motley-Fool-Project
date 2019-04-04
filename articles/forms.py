from django import forms


class CommentForm(forms.Form):
    article_uuid = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
