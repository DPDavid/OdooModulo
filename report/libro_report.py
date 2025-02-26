from odoo import models, api

class ReportLibrosDisponibles(models.AbstractModel):
    _name = 'report.libreria_libro.report_libro_biblioteca'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs= self.env['libreria_libro'].search([('status', '>', 0)])
        return {
            'doc_ids': docids,
            'doc_model': 'libreria_libro',
            'docs': docs,
        }