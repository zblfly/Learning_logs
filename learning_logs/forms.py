from socket import fromshare
from typing import Text
from django import forms
from matplotlib import widgets

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} #通过让Django使用forms.Textarea定制字段的输入小部分，讲宽度设置为80；