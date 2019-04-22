# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'TEST_ver01',
    'version' : '1.1',
    'summary': 'Test version01',
    'sequence': 1,
    'description': """
Test Pscloud    """,
    'category': 'TestVer01',
    'website': 'https://www.odoo.com/page/billing',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : [],
    'data': [
        'views/views.xml',
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'qweb': [
        # "static/src/xml/account_reconciliation.xml",
        # "static/src/xml/account_payment.xml",
        # "static/src/xml/account_report_backend.xml",
        # "static/src/xml/account_dashboard_setup_bar.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': '_auto_install_l10n',
}
