{
    'name': "Jasara E-Invoice ",
    'author':
        'ENZAPPS',
    'summary': """
This module is for Jasara.
""",

    'description': """
        This module is for Jasara.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    # 'depends': ['base','account','sale','contacts','mrp','project','enz_system_config','ubl_mail','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_payment_partner','account_invoice_import_ubl','account_invoice_ubl'],
    'depends': ['base','account','sale','contacts','mrp','project','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_payment_partner','account_invoice_import_ubl','account_invoice_ubl'],
    "images": ['static/description/icon.png'],
    'data': [
            'views/account_move.xml',
            'reports/report.xml',
            'reports/report_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
