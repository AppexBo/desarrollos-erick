from odoo import models, fields, api

class MotivoDeViaje(models.Model):
    _name = 'motivo.de.viaje'
    _description = 'Motivo de Viaje'
    
    name = fields.Char(string='Motivo', required=True)
    
    crm_line_ids = fields.One2many('crm.lead', 'motivo_de_viaje_id', 'CRM Lines')