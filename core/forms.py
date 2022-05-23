from django import forms
from django.core.validators import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(max_length=155,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your subject'}))
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 4, 'placeholder': 'your message'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')

        if name == subject:
            raise ValidationError('Subject should not be equal to name.', code='invalid_name_subject')
