from openerp import models, fields, api

class theonchange(models.Model):
    _name = 'product.model'
    amount = fields.Float('Buy Price')
    unit_price=fields.Float('Shipping price')
    price =fields.Float('standard price')


    @api.onchange('amount', 'unit_price')
        def _onchange_price(self):
            # set auto-changing field
            self.price = self.amount * self.unit_price
            # Can optionally return a warning and domains
            return True