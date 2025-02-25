from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'libreria_categoria'
    _description = 'Categoría'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')