#-*- coding: utf-8 -*-
{
    'name': "Biblioteca Trabajo",
    'author': "David Díaz Pérez",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/libreria_autor_view.xml',
        'views/libreria_categoria_view.xml',
        'views/libreria_libro_view.xml',
        'views/libreria_prestamo_view.xml',
        'views/libreria_usuario_view.xml',
        'views/libreria_menu_view.xml',
        'report/prestamo_report_activo.xml',
        'report/prestamo_report_historial.xml',
        'report/libro_report.xml',
        'report/usuario_report.xml'
    ],
    'installable': True,
    'aplication': True,
}