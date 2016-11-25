# -*- coding: utf-8 -*-
{
    'name': "Odoo Timepicker",
    'summary': """
        A timepicker plugin for Odoo 8""",
    'description': """
        A timepicker plugin for Odoo 8
    """,
    'author': "Mustafa Ehsan",
    'website': "http://mustafaaloko.github.io",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'templates.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ]
}