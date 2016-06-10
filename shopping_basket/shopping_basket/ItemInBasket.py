
class ItemInBasket(object):
    """
    An item in a shopping basket.
    """
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity
    
    @property
    def description(self):
        return self._product.description
    
    @property
    def unit_price(self):
        return self._product.price
    
    @property
    def quantity(self):
        return self._quantity
        
    @property
    def total(self):
        return self._quantity * self._product.price

    def update_quantity(self, new_quantity):
        self._quantity = new_quantity
        
        
        