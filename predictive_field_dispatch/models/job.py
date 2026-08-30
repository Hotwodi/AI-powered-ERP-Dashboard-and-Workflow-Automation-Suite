from odoo import models, fields


class Job(models.Model):
    _name = 'ai.dispatch.job'
    _description = 'AI Dispatch Job'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')
