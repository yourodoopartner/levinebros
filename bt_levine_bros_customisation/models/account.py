# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    checking_account = fields.Boolean(string="Checking Account", default=False)