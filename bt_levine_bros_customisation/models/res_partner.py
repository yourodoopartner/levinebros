# -*- coding: utf-8 -*-

from odoo import api, fields, models

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

    groupe_de_taxes_description = fields.Char(string="Groupe de taxes - Description")
