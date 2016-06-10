"""
Instead of building a buy-one-get-one-free price adjuster, I decided to build
a generic adjuster that can handle various multi-buy type offers, like:
    
    buy one get one free
    buy two for the price of three
    buy three for 2.50

The MultibuyPriceAdjuster simply runs cross-references items in the basket 
against all of the MultibuyOffers.

A MultibuyOffer is a single offer (e.g. "two bananas for the price of one").

A MultibuyOffer works by specifying items covered (as these offers sometimes 
cover multiple different products in offer), quantity which triggers the
discount, and final price for that quantity. This is better than specifying an
adjustment like -0.50p as it allows 3 for 2.50 type offers.

The MultibuyOffer objects are responsible for calculating the total for all items
included (e.g bogof with 3 apples, the third apple is charged std price). This
keeps the MultibuyPriceAdjuster simple, and allows more complex offers in the 
future. (open/closed principle).

The ItemsInOffersCollector is used internally by MultibuyPriceAdjuster to collect
items against offers (outsourcing work).

It is best to group all such offers into a single MultibuyPriceAdjuster which is
passed to a BasketWithDiscounts. That way it can detect if an item is covered
by more that one multi-buy offer, and raise an Exception.


"""

import uuid

class MultibuyPriceAdjuster(object):
    """
    Adjusts the price for a series of multi-buy offers.
    """
    def __init__(self):
        self._offers = []
        
    def add_offer(self, offer):
        """
        Adds a multi-buy offer to apply.
        """
        self._offers.append(offer)
    
    def get_adjusted_price(self, previous_total, items):
        """
        Returns the price for all items after applying offers.
        """
        collector = ItemsInOffersCollector(self._offers)
        old_value_of_items_in_offers = 0
        
        for item in items:
            if collector.item_will_be_included_in_an_offer(item):
                collector.include_item_in_offer(item)
                old_value_of_items_in_offers += item.total
                
        new_value_of_items_in_offers = collector.get_new_value_for_all()
        return (previous_total - old_value_of_items_in_offers) + \
                new_value_of_items_in_offers
    
           
class ItemsInOffersCollector(object):
    """
    Collects all items under offer for a single run of get_adjusted_price.
    """
    
    def __init__(self, offers):
        self._offers = offers
        self._items_in_offers = {}
            
    def item_will_be_included_in_an_offer(self, item):
        """
        Tests whether an item will be included in any of the  offers
        """
        for offer in self._offers:
            if offer.is_item_included(item):
                return True
        return False
    
    def include_item_in_offer(self, item):
        """
        Adds the item to its offer.
        Raises MoreThanOneMatchingOfferException if more than one offer match 
        the item.
        """
        matching_offer = None
        for offer in self._offers:
            if offer.is_item_included(item):
                if matching_offer is None:
                    matching_offer = offer
                else:
                    raise MoreThanOneMatchingOfferException(matching_offer, 
                        matching_offer, offer)
        items_in_offer = self._items_in_offers.setdefault(matching_offer, [])
        items_in_offer.append(item)
        
    def get_new_value_for_all(self):
        total = 0
        for offer, items in self._items_in_offers.iteritems():
            total += offer.total_value_for_items(items)
        return total
    
        
class MultibuyOffer(object):
    """
    A multi-buy offer, which could be:
        buy one get one free
        buy two for the price of three
        etc...
    Implements __hash__ and __eq___ so it can be used as dictionary key.
    """
    
    def __init__(self, descriptions, quantity, price_for_that_quantity):
        """
        descriptions: the descriptions to which the offer applies.
        quantity: the quantity of items to get the discount
        price_for_that_quantity: the price for that quantity.
        
        If apples cost 3.5 and you want a bogof, set:
            quantity=2
            price_for_that_quantity=3.5
        """
        self._descriptions = descriptions[:]
        self._quantity = quantity
        self._price_for_that_quantity = price_for_that_quantity
        self._id = str(uuid.uuid4())
        
    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return self._id == other._id
    
    def is_item_included(self, item):
        """
        item: ItemInBasket
        Determines if an item is included in this offer.
        """
        return item.description in self._descriptions
    
    def total_value_for_items(self, items_in_offer):
        """
        items: list of ItemInBasket
        Returns the total for all items included in the offer, including
        those to which the discount does not apply.
        """
        item_count = sum([item.quantity for item in items_in_offer])
        discounted_groups = item_count // self._quantity
        remainder_count = item_count % self._quantity
        discounted_groups_value = discounted_groups * self._price_for_that_quantity
        remainder_value = self._get_remainder_value(remainder_count, items_in_offer)
        return discounted_groups_value + remainder_value
        
    def _get_remainder_value(self, remainder_count, items_in_offer):
        """
        Returns the value for items not included in offer, e.g. third apple in
        bogof deal.
        Follows the supermarket rule of including the cheapest items in the 
        discount, and excluding the most expensive.
        """
        unpacked_individual_item_prices = []
        for item in items_in_offer:
            for i in range(item.quantity):
                 unpacked_individual_item_prices.append(item.unit_price)
        unpacked_individual_item_prices.sort(reverse=True)
        return sum(unpacked_individual_item_prices[:remainder_count])        
    

class MoreThanOneMatchingOfferException(BaseException):
    
    def __init__(self, item, offer1, offer2):
        msg = "Item ${0} is covered by multiple multibuy offers: ${1}, ${2}"
        self.message =  msg.format(item.description, offer1, offer2)
        
