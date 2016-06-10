import pytest
from logic import * 

class PriceAdjusterAddFifty:
    
    def get_adjusted_price(self, previous_total, items):
        return previous_total + (previous_total / 2)
    
class PriceAdjusterFreeLemons:
    
    def get_adjusted_price(self, previous_total, items):
        total = previous_total
        for item in items:
            if item.description == "lemon":
                total -= item.total  
        return total
    
class TestBasketWithDiscount:
    
    def test_without_adjusters(self):
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.net_total == 4 + 6
      
    def test_with_one_adjuster(self):
        """
        Should add 50% to the total.
        """
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_price_adjuster(PriceAdjusterAddFifty())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.net_total == 15
          
    def test_with_two_adjusters(self):
        """
        Should add 50% after making all lemons free.
        lemons total: 6
        apples total: 10
        final total if 50% first (wrong): 24 - 6 = 18
        final total if 50% after (correct): 15
        """
        apple = Product('apple', 5)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_price_adjuster(PriceAdjusterFreeLemons())
        basket.add_price_adjuster(PriceAdjusterAddFifty())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.net_total == 15
        
    def test_with_two_adjusters_reversed(self):
        """
        Should add 50% THEN make all lemons free.
        lemons total: 6
        apples total: 10
        final total if 50% first (correct): 24 - 6 = 18
        final total if 50% after (wrong): 15
        """
        apple = Product('apple', 5)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_price_adjuster(PriceAdjusterAddFifty())
        basket.add_price_adjuster(PriceAdjusterFreeLemons())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.net_total == 18
        
        
        
        