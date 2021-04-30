# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'sale.order' 
    
    customer_street = fields.Char(related="partner_id.street", string="Customer Street", store=True)
    replace_delivery_addr_with_invoice = fields.Boolean(string="Replace Delivery Address with Invoice", default=False)
    
    @api.onchange("replace_delivery_addr_with_invoice")
    def _onchange_replace_delivery_addr_with_invoice(self):
        if self.replace_delivery_addr_with_invoice:
            self.partner_shipping_id = self.partner_invoice_id
    