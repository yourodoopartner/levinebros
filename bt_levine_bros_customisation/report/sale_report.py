# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    residential_commercial = fields.Selection([("R", "Residential"), ("C", "Commercial"), ("none", "None")],string="Residential/Commercial")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['residential_commercial'] = ", partner.residential_commercial as residential_commercial"
        groupby += ', partner.residential_commercial'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
