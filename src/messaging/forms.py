from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select a user")

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']