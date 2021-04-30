# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.osv import expression

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    import_id = fields.Integer(string="Import_id")
    code = fields.Char(string="Code")
    bni = fields.Boolean(string="B.N.I", default=False)
    plomberie_lachine = fields.Boolean(string="Plomberie Lachine", default=False)
    assurance = fields.Boolean(string="ASSURANCE", default=False)
    henry = fields.Boolean(string="HENRY", default=False)
    a_de_gagne = fields.Boolean(string="A DE GAGNE", default=False)
    extension = fields.Char(string="Extension")
    residential_commercial = fields.Selection([("R", "Residential"), ("C", "Commercial"), ("none", "None")],string="Residential/Commercial")

#     groupe_de_taxes_description = fields.Char(string="Groupe de taxes - Description")
    expense_account_code_description = fields.Char(string="Compte de dépenses - Code et description")
    
    customer_referral = fields.Selection(
        [("google", "Google"),
         ("yelp", "Yelp"),
         ("friend", "Friend"),
         ("yellow_pages", "Yellow Pages"),
         ("bni", "B.N.I"),
         ("truck", "Truck"),
         ("facebook", "Facebook"),
         ("linkedin", "Linkedin"),
         ("instagram", "Instagram")], string="Customer referral")
    preferred_lang = fields.Selection([("English", "English"), ("Francais", "Francais")], string="Preferred Language")
    
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('street', operator, name)]
        partner_ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return models.lazy_name_get(self.browse(partner_ids).with_user(name_get_uid))
    
    
    
    
    
