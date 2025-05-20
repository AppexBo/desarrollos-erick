from odoo import models, fields, api

class Profession(models.Model):
    _name = 'profession'
    _description = 'Profesión'
    
    name = fields.Char(string='Nombre de la Profesión', required=True)
    
    partner_line_ids = fields.One2many('res.partner', 'profession_id', 'Contactos')
