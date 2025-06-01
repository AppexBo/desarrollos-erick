from odoo import models, fields

class PosPayment(models.Model):
    _inherit = 'pos.payment'

    # En tu modelo pos.payment (pos_payment.py)
    cashier_id = fields.Many2one(
        'res.users',
        string='Cajero',
        related='session_id.user_id',
        readonly=True,
        store=False
    )