from odoo import models, fields

class dynamic_approval(models.Model):
    _name = 'dynamic_approval.dynamic_approval'
    _description = 'dynamic_approval.dynamic_approval'

    dynamic_approval_field = fields.Boolean(
        string = "Dynamic Approval"
        )
    total_amount = fields.Boolean(
        string = "Total Amount"
        )
    untaxed_amounts = fields.Boolean(
        string = "Untaxed Amount"
        )

    def approval_configuration(self):


