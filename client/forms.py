from django.forms import ModelForm
from django import forms
from client.models import Video, Branch


class BranchForm(ModelForm):
    class Meta:
        model = Branch


class VideoForm(ModelForm):
    class Meta:
        model = Video
