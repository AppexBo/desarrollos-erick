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

    payment_method_name = fields.Char(
        'pos.payment',
        string='Método de pago',
        related='payment_method_id.name',
        readonly=True,
        store=False
    )