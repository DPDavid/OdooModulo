from odoo import models, api

class ReportPrestamoActivo(models.AbstractModel):
    _name = 'report.libreria_prestamo.report_prestamo_biblioteca'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs= self.env['libreria_prestamo'].search([('status', '=', 'pending')])
        return {
            'doc_ids': docids,
            'doc_model': 'libreria_prestamo',
            'docs': docs,
        }