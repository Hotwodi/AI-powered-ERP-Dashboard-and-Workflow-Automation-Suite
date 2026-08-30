{
    'name': 'AI Accounting & Financial Close Automation Suite',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'Automate month-end close, reconciliations, and AI-driven variance analysis.',
    'description': '''
        AI-powered accounting automation for financial close, reconciliations, anomaly detection, and reporting.
        =====================================================
        Automate month-end close, reconciliations, and AI-driven variance analysis.
    ''',
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 199.0,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/ai_accounting_financial_close_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
