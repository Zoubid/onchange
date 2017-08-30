from openerp import models, fields, api

class Todoonchange(models.Model):
	_name = 'product.model'
	costprice = fields.Float('Buy Price')
	shippingcost=fields.Float('Shipping price')
	total =fields.Float('standard price')


	@api.onchange('costprice','shippingcost')
	def onchange_function(self):
			self.total= self.costprice + self.shippingcost
			return total