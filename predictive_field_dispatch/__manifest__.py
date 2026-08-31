{
    'name': 'Predictive Field Dispatch Optimizer',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'Optimize technician routes, skill matching, and ETA predictions.',
    'description': '''
        Predictive dispatch optimizer for field service: route, skill, availability, and ETA optimization.
        =====================================================
        Optimize technician routes, skill matching, and ETA predictions.
    ''',
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 149.0,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/predictive_field_dispatch_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
