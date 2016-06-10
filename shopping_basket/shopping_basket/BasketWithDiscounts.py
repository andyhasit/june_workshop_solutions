"""
This is a shopping basket that allows the applying of various price adjustments,
which can be discounts, or adding things like tax.

This is more flexible than one function which applies the three discounts 
required from the spec.

 
I implemented this as separate a class to BasicBasket using object composition
instead of inheritance, i.e. it uses an "inner basket" instead of subclassing
BasicShoppingBasket.

Advantages:
    
    It's easier to test. We can pass it a mock inner basket with just the basic 
    functionality needed to test the calculation of totals.
    
    In production we can pass an inner basket which persists changes to the 
    database, and still trust it will behave the same.
    
    We can build other types of shopping basket which use an inner basket without
    affecting this one
    
All of the above would be difficult if we implemented the discount calculations
in the same class as BasicBasket, or inherited from it.

"""

class BasketWithDiscounts(object):
    """
    A shopping which allows adding of price adjusters, which may be discounts.
    """
    
    def __init__(self, inner_basket):
        """
        inner_basket must be an implementation of BasicBasket.
        """
        self._basket = inner_basket
        self._price_adjusters = []
        
    def add_price_adjuster(self, price_adjuster):
        """
        price_adjuster must be an implementation of BasePriceAdjuster.
        Price adjusters will be applied when caculating the total in the order
        they were added here. Caller is responsible for ensuring correct order.
        """
        self._price_adjusters.append(price_adjuster)
        
    @property
    def net_total(self):
        """
        The total after applying all adjustments (in order they were added).
        """
        total = self._basket.total
        items = self._basket.items
        for price_adjuster in self._price_adjusters:
            total = price_adjuster.get_adjusted_price(total, items)
        return total
        
    @property
    def gross_total(self):
        """
        The total before applying any adjustments.
        """
        return self._basket.total
        
    @property
    def items(self):
        return self._basket.items
    
    def add_item(self, product, quantity):
        return self._basket.add_item(product, quantity)
    
    def remove_item(self, item_in_basket):
        self._basket.remove_item(item_in_basket)
        
    def empty(self):
        self._basket.empty()
        
        
        
        