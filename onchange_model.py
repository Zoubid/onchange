from openerp import models, fields, api

class theonchange(models.Model):
    _name = 'product.model'
    amount = fields.Float('Buy Price',0)
    unit_price=fields.Float('Shipping price',0)
    price =fields.Float('standard price',0)


    # @api.multi
    @api.onchange('amount', 'unit_price')
    def _onchange_price(self):
        # set auto-changing field
        result = self.amount * self.unit_price
        self.price =result
        # Can optionally return a warning and domains