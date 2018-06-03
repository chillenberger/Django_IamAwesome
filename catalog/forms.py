from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Story
from django.core.files import File
from croppie.fields import Croppiefield
import boto3
import os

class NewStoryForm(forms.ModelForm):
    photo = CroppieField()

    class Meta:
        model = Story
        fields = ['title', 'story', 'photo']
