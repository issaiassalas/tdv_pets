
{
    'name': 'Mis Mascotas',
    'version': '0.0.1',
    'description': 'Cosas de mascotas',
    'summary': 'Sumario de cosas de mascotas',
    'depends': ['base', 'contacts'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'reports/pet_action_report.xml',
        'views/pet_action.xml',
        'views/pet_views.xml',
        'views/menu.xml',
    ]
}