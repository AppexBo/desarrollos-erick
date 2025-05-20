from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    estado_civil_id = fields.Many2one(
        "estado.civil", 
        string="Estado Civil", 
        required=False
    )

    nationality_id = fields.Many2one(
        "res.country", 
        "Nacionalidad"
    )

    profession_id = fields.Many2one(
        "profession", 
        string="Profesión", 
        required=False
    )

    birthday = fields.Date(
        string='Fecha de nacimiento', 
        required=True
    )