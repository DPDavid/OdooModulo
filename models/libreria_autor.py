from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'libreria_autor'
    _description = 'Autor'

    name = fields.Char(string='Nombre', required=True)
    biography = fields.Text(string='Biografía')
