# -*- coding: utf-8 -*-
{
    'name': 'Search Product Wizard',
    'author': 'Aktiv Software',
    'category': 'Stock',
    'website': 'www.aktivsoftware.com',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'summary': '''
                This module helps in finding a matching product
                                as per its attribute.
            ''',
    'description': '''
                    The Module - Search Product Wizard is purposefully
                    developed to ease the end user in finding a
                    relevant product as per the Product Attributes
                    and its Values by generating a Report based on the same.
                    Settings of the Product Attributes are being
                    maintained from Configurations. A Package with the
                    entered quantity of the relevant product will be
                    created and will generate a consequent Lot Number.
                ''',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'wizard/search_product_view.xml',
        'report/search_product_report_registration.xml',
        'report/search_product_template.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': False
}
