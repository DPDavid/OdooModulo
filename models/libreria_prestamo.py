from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class LibraryLoan(models.Model):
    _name = 'libreria_prestamo'
    _description = 'Préstamo de Libros'

    user_id = fields.Many2one('libreria_usuario', string='Usuario', required=True)
    book_id = fields.Many2one('libreria_libro', string='Libro', required=True)
    loan_date = fields.Date(string='Fecha de Préstamo', default=fields.Date.today)
    return_date = fields.Date(string='Fecha de Devolución', compute='_compute_return_date', store=True)
    status = fields.Selection([
        ('pending', 'Pendiente'),
        ('returned', 'Devuelto'),
        ('late', 'Retrasado')
    ], string='Estado', default='pending')

    @api.depends('loan_date')
    def _compute_return_date(self):
        """ Automáticamente asignar una fecha de devolución estimada de 7 días. """
        for record in self:
            if record.loan_date:
                record.return_date = record.loan_date + timedelta(days=7)

    @api.constrains('user_id')
    def _check_user_loan_limit(self):
        """ Bloquear préstamo si el usuario ya tiene 4 libros prestados. """
        for record in self:
            active_loans = self.search_count([
                ('user_id', '=', record.user_id.id),
                ('status', '=', 'pending')
            ])
            if active_loans >= 4:  # Se mantiene el límite de 4 préstamos
                raise ValidationError("El usuario ya tiene 4 libros prestados y no puede solicitar más.")

    @api.model
    def create(self, vals):
        """ Reducir la cantidad de copias del libro al crear un préstamo. """
        book = self.env['libreria_libro'].browse(vals['book_id'])
        if book.copies <= 0:
            raise ValidationError("No hay copias disponibles de este libro.")
        book.sudo().write({'copies': book.copies - 1})  # Reducir copias disponibles
        return super(LibraryLoan, self).create(vals)

    def action_return_book(self):
        """ Registrar la devolución del libro y actualizar copias disponibles. """
        for loan in self:
            if loan.status != 'returned':  
                loan.status = 'returned'
                if loan.book_id:
                    loan.book_id.sudo().write({'copies': loan.book_id.copies + 1})  # Aumentar copias disponibles

    @api.onchange('status')
    def _onchange_status(self):
        """ Manejar cambios manuales en el estado del préstamo y actualizar copias disponibles. """
        for record in self:
            if not record.book_id:
                return
            
            if record.status == 'returned' and record.book_id:
                record.book_id.sudo().write({'copies': record.book_id.copies + 1})  # Aumentar copias
            elif record.status == 'pending':
                if record.book_id.copies > 0:
                    record.book_id.sudo().write({'copies': record.book_id.copies - 1})  # Reducir copias
                else:
                    raise ValidationError("No hay copias disponibles para prestar este libro.")

    @api.depends('status')
    def _compute_hide_return(self):
        """ Ocultar botón si el libro ya fue devuelto """
        for record in self:
            record.hide_return = record.status == 'returned'

    hide_return = fields.Boolean(compute="_compute_hide_return")