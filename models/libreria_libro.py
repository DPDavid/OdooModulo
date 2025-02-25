from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'libreria_libro'
    _description = 'Libro'
    _rec_name = 'title'

    title = fields.Char(string="Título", required=True)
    author = fields.Many2one('libreria_autor', string="Autor", required=True)
    category = fields.Many2one('libreria_categoria', string="Categoría", required=True)
    isbn = fields.Char(string="ISBN")
    copies = fields.Integer(string="Copias disponibles", default=1)
