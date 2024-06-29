from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_status = fields.Char('Delivery Status', compute='_compute_delivery_status')

    def _compute_delivery_status(self):
        for record in self:
            if record.picking_ids:
                for picking in record.picking_ids:
                    status = dict(picking.fields_get(allfields=['state'])['state']['selection'])[picking.state]
                    record.delivery_status = status
            else:
                record.delivery_status = False
