# -*- coding: utf-8 -*-
"""
Enables the user to add style plugin that displays a html tag with
the provided settings from the style plugin.
"""
from __future__ import unicode_literals
import urllib
from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_attributes_field.fields import AttributesField
from django.utils.text import slugify


@python_2_unicode_compatible
class CodePrettify(CMSPlugin):

    lang = models.CharField(
        verbose_name=_('Code Language'),
        max_length=100,
        blank=True,
        null=True,
    )

    skin = models.CharField(
        verbose_name=_('Skin'),
        max_length=100,
        blank=True,
        null=True,
    )

    linenums = models.BooleanField(
        verbose_name=_('Line Numbers'),
        default=True,
    )

    show_all_linenums = models.BooleanField(
        verbose_name=_('Show All Line Numbers'),
        default=False,
    )

    start_linenum = models.PositiveIntegerField(
        verbose_name=_('Optional Start Line Number'),
        blank=True,
        null=True,
    )

    autorun = models.BooleanField(
        verbose_name=_('Run automatically on page load'),
        default=True,
    )

    code = models.TextField(
        verbose_name=_('Code'),
        blank=True,
        null=True,
    )

    # Default id/classes/attributes
    # --------------------------------
    id_name = models.CharField(
        verbose_name=_('ID name'),
        blank=True,
        null=True,
        max_length=255,
    )
    additional_classes = models.CharField(
        verbose_name=_('Additional classes'),
        blank=True,
        max_length=255,
        help_text=_('Additional comma separated list of classes '
            'to be added to the element e.g. "row, column-12, clearfix".'),
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class', 'id', 'style'],
    )

    def clean(self):
        if self.id_name:
            valid_id_name = slugify(self.id_name)
            self.id_name = valid_id_name

    def get_additional_classes(self):
        return ' '.join(item.strip() for item in self.additional_classes.split(',') if item.strip())

    @property
    def get_id_name(self):
        return self.id_name or str(self.pk)

    def __str__(self):
        return self.get_id_name

    def url_params_dict(self):
        return {
            'autorun': self.autorun,
            'lang': self.lang,
            'skin': self.skin,
        }

    def get_url_params(self):
        return "?" + urllib.parse.urlencode(self.url_params_dict())
