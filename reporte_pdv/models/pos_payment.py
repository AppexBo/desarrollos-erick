from odoo import models, fields

class PosPayment(models.Model):
    _inherit = 'pos.payment'

    # En tu modelo pos.payment (pos_payment.py)
    cashier_id = fields.Many2one(
        'hr.employee',
        string='Cajero',
        related='pos_order_id.employee_id',
        readonly=True,
        store=False
    )