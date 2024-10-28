from odoo import models, fields

class approval_configuration(models.Model):
    _name = 'dynamic_approval.approval_configuration'
    _description = 'dynamic_approval.dynamic_approval'

    minimum_amount = fields.Float(
        string = 'Minimum Amount'
        )
    buyer_always_in_cc = fields.Boolean(
        string = "Buyer Always in cc"
        )

    
