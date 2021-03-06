# -*- coding: utf-8 -*-

from flectra import models, fields, api

class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.one
    def _get_amount_residual(self):
        advance_amount = 0.0
        for line in self.account_payment_ids:
            if line.state != 'draft':
                advance_amount += line.amount
        self.amount_residual = self.amount_total - advance_amount

    account_payment_ids = fields.One2many('account.payment', 'sale_id',
                                          string="Pay sale advanced",
                                          readonly=True)
    amount_residual = fields.Float('Residual amount', readonly=True,
                                   compute="_get_amount_residual")
