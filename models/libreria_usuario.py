from odoo import models, fields

class LibraryUser(models.Model):
    _name = 'libreria_usuario'
    _description = 'Usuario de Biblioteca'

    name = fields.Char(string='Nombre Completo', required=True)
    email = fields.Char(string='Correo Electrónico')
    phone = fields.Char(string='Teléfono')
    registration_date = fields.Date(string='Fecha de Registro', default=fields.Date.today)