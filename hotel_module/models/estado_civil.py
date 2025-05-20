from odoo import models, fields, api

class EstadoCivil(models.Model):
    _name = 'estado.civil'
    _description = 'Estado Civil'
    
    name = fields.Char(string='Nombre del Estado', required=True)
    
    partner_line_ids = fields.One2many('res.partner', 'estado_civil_id', 'Contactos')
