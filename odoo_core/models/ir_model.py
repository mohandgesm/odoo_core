
from odoo import fields, models


class IrModel(models.Model):
    _inherit = "ir.model"
    
    actions_ids = fields.One2many('ir.actions.actions', compute='_from_actions_ids', string='Actions')
    
    def _from_actions_ids(self):
        for model in self:
            model.actions_ids = self.env['ir.actions.actions'].search([('binding_model_id', '=', model.id)])