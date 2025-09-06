
from odoo import fields, models


class IrActions(models.Model):
    _inherit = "ir.actions.actions"
    
    external_xml_id = fields.Char(compute='_compute_external_xml_id',string="External ID") 
    
    def _compute_external_xml_id(self):
        for record in self:
            action = self.env[record.type].search([('id','=',record.id)])
            res =  action.get_external_id()
            record.external_xml_id = res.get(record.id)