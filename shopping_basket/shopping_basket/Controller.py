from Product import Product
from BasicBasket import BasicBasket
from BasketWithDiscounts import BasketWithDiscounts
from MultibuyPriceAdjuster import MultibuyPriceAdjuster

class Controller(object):
    """
    The main controller for the application.
    This is the only object the UI has a reference to (initially).
    It ensures new products have unique descriptions (currently products can 
    only be added, not edited or removed)
    """
    def __init__(self):
        self._products = []
        self._used_descriptions = []
        self._unique_desc_error_message = \
                "Description ${0} is already claimed by an other product"
        self._offers = []
        
    def get_products(self):
        return self._products[:]
    
    def new_product(self, description, price):
        if description in self._used_descriptions:
            raise ValueError(self._unique_desc_error_message.format(description))
        self._used_descriptions.append(description)
        new_product = Product(description, price)
        self._products.append(new_product)
        return new_product
     
    def new_basket(self):
        """
        Creates a new shopping basket. Still need to add price adjustments.
        """
        return BasketWithDiscounts(BasicBasket())
    
    
        
        
        
        
        
        