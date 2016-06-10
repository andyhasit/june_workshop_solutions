class Product(object):
    """
    A product in the shop. Descriptions must be unique, handle elsewhere.
    """
    
    def __init__(self, description, price):
        self._description = description
        self._price = price
    
    @property
    def description(self):
        return self._description
    
    @property
    def price(self):
        return self._price