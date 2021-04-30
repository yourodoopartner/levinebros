# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    checking_account = fields.Boolean(string="Checking Account", default=False)

class AccountPayment(models.Model):
    _inherit = 'account.payment'
    
    payment_source = fields.Selection(
        [("cash", "Cash"),
         ("check", "Check"),
         ("etransfer", "eTransfer"),
         ("cc", "CC"),
         ("web_cc", "Web CC"),
         ("phone_cc", "Phone CC"),
         ("mail_cc", "Mail CC"),
         ("paypal", "Paypal"),
         ("direct_deposit", "Direct Deposit")], string="Payment Source")
    
class AccountMove(models.Model):
    _inherit = 'account.move' 
    
    customer_street = fields.Char(related="partner_id.street", string="Customer Street", store=True)
    
    partner_shipping_id = fields.Many2one(
        'res.partner',
        string='Delivery Address',
        readonly=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Delivery address for current invoice.")
    client_po = fields.Char(string="Client PO")
    
    
    @api.model_create_multi
    def create(self, vals_list):
        product_ids = self.env['product.product'].search([('labour', '=', True)])
        for vals in vals_list:
            if product_ids:
                if 'invoice_line_ids' in vals:
                    vals['invoice_line_ids'].append((0, 0, {
                        'display_type': 'line_section',
                        'name':'Labour',
                        'debit': False,
                        'credit': False,
                        'price_unit': False,
                        'quantity': False,
                        'account_id': False,
                        }))
                else:
                    vals['invoice_line_ids'] = [(0, 0, {
                        'display_type': 'line_section',
                        'name':'Labour',
                        'debit': False,
                        'credit': False,
                        'price_unit': False,
                        'quantity': False,
                        'account_id': False,
                        })]
                for product in product_ids:
                    invoice_line_vals = {
                    'name': product.name,
                    'price_unit': product.lst_price or 0.0,
                    'quantity': 1.0,
                    'product_id': product.id,
                    'product_uom_id': product.uom_id.id,
                    }
                    vals['invoice_line_ids'].append((0, 0, invoice_line_vals))
        return super(AccountMove, self).create(vals_list)
    
    