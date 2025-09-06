# -*- coding: utf-8 -*-
{
    'name': "Odoo core",
    'version': '18.0.1.0.0',

   'version': '18.0.1.0.0',
    'summary': 'A comprehensive tool for managing a model\'s actions.',
    'description': """
                This module is designed for Odoo developers and administrators who need to quickly audit and manage all actions related to a specific model. By adding a dedicated tab to the "Models" menu, it provides a centralized view of all window actions, server actions, and report actions that are bound to a model, significantly simplifying the development and maintenance workflow.

                Key Features:
                - New "Actions" Tab: Adds a dedicated, easy-to-find tab to the ir.model form view.
                - Comprehensive Listing: Displays all types of ir.actions records (act_window, server, report, etc.) that are bound to the current model.
                - External ID Visibility: Shows the External XML ID for each action, which is essential for development, data import/export, and version control.
                - Simplified Navigation: Provides a direct link to the action's form view for quick access and editing.
                - Improved Workflow: Eliminates the need to manually search through different menus to find all related actions for a model.

                How It Works:
                1. Navigate to Settings > Technical > Database Structure > Models.
                2. Select any model from the list (e.g., Contacts, Sale Order).
                3. A new "Actions" tab will now be visible on the form view.
                4. Click the "Actions" tab to see a list of all actions bound to the selected model.
                5. You can click on any action in the list to open and edit its form.

                Benefits for Odoo Professionals:
                This module transforms a time-consuming administrative task into a single-click operation. It is a must-have for any Odoo developer, consultant, or administrator who needs to maintain and understand the structure of complex Odoo applications.
""",

    'author': "GK Software",
    'website': "https://www.google.com",
    'images': ['static/description/cover.jpg'],

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

