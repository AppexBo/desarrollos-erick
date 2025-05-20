from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = "crm.lead"

    estado_civil_id = fields.Many2one(
        "estado.civil",  # Mismo modelo que en res.partner
        string="Estado Civil",
        compute="_compute_estado_civil",
        #inverse="_inverse_estado_civil",
        store=True,
        readonly=False,
        tracking=True  # Opcional: para registrar cambios en el chatter
    )
    
    nationality_id = fields.Many2one(
        "res.country",
        string="Nacionalidad",
        compute="_compute_nationality",
        #inverse="_inverse_nationality",
        store=True,
        readonly=False,
        tracking=True
    )
    
    profession_id = fields.Many2one(
        "profession",
        string="Profesión",
        compute="_compute_profession",
        #inverse="_inverse_profession",
        store=True,
        readonly=False,
        tracking=True
    )

    birthday = fields.Date(
        string="Fecha de nacimiento",
        compute="_compute_birthday",
        inverse="_inverse_birthday",
        store=True,
        readonly=False,
        tracking=True
    )

    vat = fields.Char(
        string="Carnet de identidad o NIT",
        compute="_compute_vat",
        inverse="_inverse_vat",
        store=True,
        readonly=False,
        tracking=True
    )

    company_partner_id = fields.Many2one(
        'res.partner',
        string='Empresa/Compañía',
        domain=[('is_company', '=', True)],
    )


    is_company = fields.Boolean(
        #string='Is a Company',
        related='partner_id.is_company',
        readonly=True,
        store=True  # Opcional, si necesitas que se guarde en la BD para búsquedas
    )

    @api.depends('partner_id.is_company')
    def _compute_is_company(self):
        for lead in self:
            lead.is_company = lead.partner_id.is_company if lead.partner_id else False
            
    @api.depends("partner_id", "partner_id.birthday")
    def _compute_birthday(self):
        """Actualiza la fecha de cumpleaños cuando se selecciona un partner"""
        for lead in self:
            lead.birthday = lead.partner_id.birthday

    def _inverse_birthday(self):
        """Actualiza la fecha de cumpleaños en el partner cuando se modifica en el CRM"""
        for lead in self:
            if lead.partner_id:
                lead.partner_id.sudo().write({
                    'birthday': lead.birthday
                })

    
    @api.depends("partner_id", "partner_id.vat")
    def _compute_vat(self):
        """Actualiza el número de identificación cuando se selecciona un partner"""
        for lead in self:
            lead.vat = lead.partner_id.vat

    def _inverse_vat(self):
        """Actualiza el número de identificación en el partner cuando se modifica en el CRM"""
        for lead in self:
            if lead.partner_id:
                lead.partner_id.sudo().write({
                    'vat': lead.vat
                })

    @api.depends("partner_id", "partner_id.estado_civil_id")
    def _compute_estado_civil(self):
        """Actualiza el estado civil cuando se selecciona un partner"""
        for lead in self:
            lead.estado_civil_id = lead.partner_id.estado_civil_id

    def _inverse_estado_civil(self):
        """Actualiza el estado civil en el partner cuando se modifica en el CRM"""
        for lead in self:
            if lead.partner_id:
                lead.partner_id.sudo().write({
                    'estado_civil_id': lead.estado_civil_id.id
                })
    
    @api.depends("partner_id", "partner_id.nationality_id")
    def _compute_nationality(self):
        """Actualiza la nacionalidad cuando se selecciona un partner"""
        for lead in self:
            lead.nationality_id = lead.partner_id.nationality_id

    def _inverse_nationality(self):
        """Actualiza la nacionalidad en el partner cuando se modifica en el CRM"""
        for lead in self:
            if lead.partner_id:
                lead.partner_id.sudo().write({
                    'nationality_id': lead.nationality_id.id
                })
    
    @api.depends("partner_id", "partner_id.profession_id")
    def _compute_profession(self):
        """Actualiza la profesión cuando se selecciona un partner"""
        for lead in self:
            lead.profession_id = lead.partner_id.profession_id

    #def _inverse_profession(self):
    #    """Actualiza la profesión en el partner cuando se modifica en el CRM"""
    #    for lead in self:
    #        if lead.partner_id:
    #            lead.partner_id.sudo().write({
    #                'profession_id': lead.profession_id.id
    #            })