# -*- encoding: utf-8 -*-

{
    'name': 'Sale Passed Days',
    'author': "Kareem Abuzaid",
    'description':
        """
        A module that adds the number of days that had passed \
        since the creation of a sales order. This is intended \
        to be a short module that demonstrates good practices \
        when creating a module.
        """,
    'version': '12.0.1.0',
    'depends': ['base_setup', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'application': False,
    'auto_install': True,
}