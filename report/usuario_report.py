from odoo import models, api

class ReportUsuario(models.AbstractModel):
    _name = 'report.libreria_usuario.report_usuario_biblioteca'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs= self.env['libreria_usuario'].search([()])
        return {
            'doc_ids': docids,
            'doc_model': 'libreria_usuario',
            'docs': docs,
        }