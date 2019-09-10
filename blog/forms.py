from django import forms
from .models import Message, Response


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'message')


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('name', 'response')
