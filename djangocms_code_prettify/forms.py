from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from .consts import *


class CodePrettifyForm(ModelForm):
    lang = forms.ChoiceField(choices=LANG_CHOICES,
                             initial=LANG_CHOICES[0],
                             help_text=_("Optionally select a specific language parser"),
                             required=False)

    skin = forms.ChoiceField(choices=SKIN_CHOICES,
                             initial=SKIN_CHOICES[0],
                             required=False)


