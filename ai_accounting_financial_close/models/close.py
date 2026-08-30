from odoo import models, fields


class Close(models.Model):
    _name = 'ai.accounting.close'
    _description = 'AI Accounting Close Rule'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')
