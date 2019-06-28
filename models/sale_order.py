# -*- encoding: utf-8 -*-

from odoo import api, fields, models
from odoo.fields import Datetime


class SaleOrder(models.Model):
    """
    Inherit sale order module to add the
    days passed field.
    """
    _inherit = 'sale.order'

    days_passed = fields.Integer("Days Since Creation",
                                 compute='_compute_days_passed',
                                 readonly=True,
                                 store=True)

    @api.depends('create_date')
    def _compute_days_passed(self):
        """
        Compute the value of the days passed field.
        """
        today = Datetime.today()
        for record in self:
            record.days_passed = \
                today.day - record.create_date.day

