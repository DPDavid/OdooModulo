from odoo import models, api

class ReportPrestamoHistorial(models.AbstractModel):
    _name = 'report.libreria_prestamo.report_prestamo_historial'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs= self.env['libreria_prestamo'].search([()])
        return {
            'doc_ids': docids,
            'doc_model': 'libreria_prestamo',
            'docs': docs,
        }