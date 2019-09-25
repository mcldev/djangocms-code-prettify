# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CodePrettify
from .forms import CodePrettifyForm


class CodePrettifyPlugin(CMSPluginBase):
    model = CodePrettify
    name = _('Code Prettify')
    module = _('Generic')
    render_template = 'djangocms_code_prettify/code-prettify.html'
    form = CodePrettifyForm
    fieldsets = (
        (None, {
            'fields': (
                'lang',
                'skin',
                ('linenums', 'show_all_linenums', 'start_linenum'),
                'code'
            )
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': (
                'autorun',
                'id_name',
                'additional_classes',
                'attributes',
            ),
        }),
    )


plugin_pool.register_plugin(CodePrettifyPlugin)
