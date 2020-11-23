# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime

from odoo import api, fields, models
from odoo.osv import expression


class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        new_args = args
        for arg in args:
            if arg[0] in ('partner_id') and arg[1] == "ilike":
                dom = ['|','|','|','|','|',
                    ('name', 'ilike', arg[2]),
                    ('phone', 'ilike', arg[2]),
                    ('email', 'ilike', arg[2]),
                    ('mobile', 'ilike', arg[2]),
                    ('street', 'ilike', arg[2]),
                    ('street2', 'ilike', arg[2]),
                    ]
                partner_ids = self.env['res.partner']._search(dom)
                if partner_ids:
                    if isinstance(partner_ids, (list, tuple)):
                        new_args = expression.OR([new_args, [('partner_id', 'in', partner_ids)]])
                    elif isinstance(partner_ids, self.env['res.partner'].__class__):
                        new_args = expression.OR([new_args, [('partner_id', 'in', partner_ids.ids)]])
        args = new_args
        return super(ProjectTask, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
    
