# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.misc import format_date
from datetime import timedelta


class Task(models.Model):
    _inherit = "project.task"
    
    task_status = fields.Selection([
        ('Green', 'Service call in progress'), ('Yellow', 'Next call assigned – (Not started)'), 
        ('Pink', 'Non-urgent call'), ('Red', 'Very urgent (Heating)'), 
        ('Blue', 'Very urgent (plumbing)'), ('Purple', 'Job (Project Management job)'),
        ('Grey', 'Insurance division')
    ], 'Status')
    task_status_color = fields.Integer(compute='_compute_task_color', default=0, string='Status Colour')
    
    @api.depends('task_status')
    def _compute_task_color(self):
        for task in self:
            if task.task_status == 'Green':
                task.task_status_color = 10
            elif task.task_status == 'Yellow':
                task.task_status_color = 3
            elif task.task_status == 'Pink':
                task.task_status_color = 6
            elif task.task_status == 'Red':
                task.task_status_color = 1    
            elif task.task_status == 'Blue':
                task.task_status_color = 4    
            elif task.task_status == 'Purple':
                task.task_status_color = 11
            elif task.task_status == 'Grey':
                task.task_status_color = 8
            else:
                task.task_status_color = 0
                

