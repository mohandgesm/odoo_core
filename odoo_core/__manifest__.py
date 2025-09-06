# -*- coding: utf-8 -*-
{
    'name': "Odoo core",
    'version': '18.0.1.0.0',

    'summary': "Customization the odoo core",

    'description': """I am customize the odoo core by adding new features for odoo base module""",

    'author': "GK Software",
    'website': "https://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'GK Software',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application':True,
    'installable': True,
    'auto_install': True, # install automatically if the dependencies are installed
    'license':'LGPL-3',

    # always loaded
    'data': [
        'views/ir_model.xml',
        'views/ir_actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

