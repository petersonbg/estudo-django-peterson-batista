from asyncio import tasks
from dataclasses import fields
from django import forms
from .models import Task

class FormTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')

