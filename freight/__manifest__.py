# -*- coding: utf-8 -*-

{
    'name': 'Freight',
    'version': '1.0',
    'category': 'freight',
    'images': ['static/description/banner.jpg'],
    'author':'inteslar',
    'summary': 'Freight Management By Inteslar',
    'description': """
Key Features
------------
* Freight Management
        """,
    'depends': ['base',
                'base_setup',
                'account',
                'product',
                'web',
                'contacts',
                'mail',
                'board',
                'calendar',
                'hr'],
    'data': [
        'data/freight_data.xml','security/security.xml',
        'security/ir.model.access.csv',
        'report/bill_of_lading.xml',
        'report/airway_bill.xml',
        'views/freight_report.xml',
        'wizard/register_invoice_freight_view.xml',
        'views/freight_view.xml',
    ],
    'qweb': [
        "static/src/xml/freight_dashboard.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
