# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    part_code = fields.Char(string="Part Code")
    item_size = fields.Char(string="Item Size")
    item_component_description = fields.Char(string="Item Component Description")
    unit_of_measure = fields.Selection([
        ("E", "Per Each / Per Foot"),
        ("C", "Per Hundred"),
        ("M", "Per Thousand")],string="Unit of Measure")
#     allpriser_price = fields.Float(string="Allpriser Price")
    percent_price_change = fields.Char(string="% Price Change")
    page = fields.Char(string="Page#")
    addition_flag = fields.Boolean(string="Addition Flag")
    deletion_flag = fields.Boolean(string="Deletion Flag")
    part_code_change = fields.Boolean(string="Part Code Change")
    price_change_flag = fields.Boolean(string="Price Change Flag")
    other_edits = fields.Boolean(string="Other Edits")
    product_type_code = fields.Char(string="Product Type Code")
    product_type_description = fields.Text(string="Product Type Description")
    product_group_code = fields.Char(string="Product Group Code")
    product_group_description = fields.Text(string="Product Group Description")
    publication_code = fields.Selection([
        ("1", "Red"),
        ("2", "Gold"),
        ("3", "Blue"),
        ("4", "Silver"),
        ("5", "Yellow"),
        ("6", "Green")],string="Publication Code")
    pricing_region = fields.Selection([
        ("1", "ONT"),
        ("2", "EPQ"),
        ("3", "FPQ"),
        ("4", "ATL"),
        ("5", "MS"),
        ("6", "AB"),
        ("7", "BC"),
        ("8", "English"),
        ("9", "French"),
        ("10", "Generated from user’s catalogue")],string="Pricing Region")
    update_id = fields.Char(string="Update ID")
    date_of_update = fields.Date(string="Date of Update")
    previous_part_code = fields.Char(string="Previous Part Code")
    allpriser_key_number = fields.Char(string="Allpriser Key Number")
    effective_date = fields.Date(string="Effective Date")
    future_use_1 = fields.Char(string="Reserved for Future Use #1")
    future_use_2 = fields.Char(string="Reserved for Future Use #2")

       
    
    