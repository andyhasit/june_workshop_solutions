"""
A shopping basket demo application for CodeClan.

This file just runs a mini demo to show it works.
"""

from logic import *
from DemoHelper import DemoHelper

def run_demo():
    """
    This runs the quick demo, feel free to muck around with this.
    This isn't structured code, just a playground :-)
    """
    controller = Controller()
    basket = controller.new_basket()
    helper = DemoHelper(basket)
    user_has_loyalty_card = True
    
    # Create some products in our shop
    # Uniqueness is determined by description (e.g. "apple") because this is
    # just a demo, and it's simpler like that.
    
    apple = controller.new_product('apple', 1.50)
    orange = controller.new_product('orange', 2.00)
    lemon = controller.new_product('lemon', 2.25)
    pear = controller.new_product('pear', 1.00)
    
    # Create the price adjuster for multi-buy offers (e.g. bogof on apples)
    # Price adjusters can be used for discounts or increases (like tax)
    # We'll add them to the basket further down .
    # This one takes care of all "multi-buy" offers, of which bogof is but one
    # example. It also raises an exception if offers clash.
    
    multi_buy_price_adjuster = MultibuyPriceAdjuster()
    
    # Create a bogof offer on apples
     
    bogof_apple_offer = MultibuyOffer(['apple'], 2, apple.price)
    
    # Add that offer to the price adjuster for multi-buy offers
    # Note: we could add more offers here, like buy 3 apples for 2:
    #
    #    three_apples_for_two = MultibuyOffer(['apple'], 3, apple.price * 2)
    #
    # Or 4 citrus for 3 pounds (because it happens!)
    #
    #    four_citrus_for_three_pounds = MultibuyOffer(['lemon', 'orange'], 4, 3.00)
    
    multi_buy_price_adjuster.add_offer(bogof_apple_offer)
    
    # Create 10% off price adjuster for value over 20 
    
    ten_percent_off_on_orders_over_twenty = PercentagePriceAdjuster(10, 20)
    
    # Create 10% off price adjuster for customers with loyalty cards, no minimum.
    
    user_loyalty_discount = PercentagePriceAdjuster(2)
    
    # Add price adjusters in the order we want them applied
    
    basket.add_price_adjuster(multi_buy_price_adjuster)
    basket.add_price_adjuster(ten_percent_off_on_orders_over_twenty)
    if user_has_loyalty_card:
        basket.add_price_adjuster(user_loyalty_discount)  
    
    # We're now ready to start using the basket!
    
    # Add, remove & show basic 2% discount
    
    basket.empty()
    basket.add_item(pear, 10)
    apple_entry = basket.add_item(apple, 100)
    basket.remove_item(apple_entry)
    helper.print_basket("10 pears, with 2% discount")
    
    # Adding multiple items of same type consolidates values
    
    basket.empty()
    basket.add_item(orange, 6)
    basket.add_item(orange, 6)
    helper.print_basket("12 oranges, with 10% then 2% discount (21.168)")
    
    # Adding items with bogof
    
    basket.empty()
    basket.add_item(apple, 5)
    helper.print_basket("5 apples at 1.50, 2 cancelled out = 4.50, then 2%")
    
    # You can add more examples below, or tweak the above...
    
    
# This file is always __main__ so:
run_demo()
