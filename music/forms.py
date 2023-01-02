from django import forms
from account.models import Review


class CommentForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
                           'class': 'form-control', 'id': 'message', 'placeholder': 'Your message'}), max_length=500)

    class Meta:
        model = Review
        fields = ('text',)

