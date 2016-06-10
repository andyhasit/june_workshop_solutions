import pytest
from logic import * 

class TestMultibuyPriceAdjuster:
    
        
    @pytest.fixture
    def items(self):
        apple = Product('apple', 2)
        orange = Product('orange', 1.50)
        lemon = Product('lemon', 1.50)
        grapefruit = Product('grapefruit', 1.25)
        return [
                ItemInBasket(apple, 3),
                ItemInBasket(orange, 2), 
                ItemInBasket(lemon, 4), 
                ItemInBasket(grapefruit, 1)
                ]
        
    def normal_total(self, items):
        return sum([x.total for x in items])
        
    def test_multibuy_no_offers(self, items):
        """
        No offers, should return the normal price.
        """
        adjuster = MultibuyPriceAdjuster()
        assert adjuster.get_adjusted_price(25, items) == 25
        assert adjuster.get_adjusted_price(37, items) == 37
        
    def test_multibuy_bogof_single(self, items):
        """
        bogof on oranges. items has 2 oranges at 1.50 so
        total should be total - 1.50.
        """
        bogof_citrus = MultibuyOffer(['orange'], 2, 1.50)
        adjuster = MultibuyPriceAdjuster()
        adjuster.add_offer(bogof_citrus)
        normal_total = self.normal_total(items)
        new_total = adjuster.get_adjusted_price(normal_total, items) 
        assert new_total == normal_total - 1.50 
  
    def test_multibuy_discount_on_odd_number(self, items):
        """
        items has 3 apples at 2 so .
        """
        apples_two_for_three_pounds = MultibuyOffer(['apple'], 2, 3)
        adjuster = MultibuyPriceAdjuster()
        adjuster.add_offer(apples_two_for_three_pounds)
        normal_total = self.normal_total(items)
        new_total = adjuster.get_adjusted_price(normal_total, items)
        old_price_for_items = 6
        new_price_for_items = 3 + 2 # deal plus spare apple
        assert new_total == normal_total - (old_price_for_items - new_price_for_items)
        
    def test_multibuy_discount_on_four(self, items):
        """
        items has 4 lemon at 1.50 so 
        """
        lemons_bogof = MultibuyOffer(['lemon'], 2, 1.5)
        adjuster = MultibuyPriceAdjuster()
        adjuster.add_offer(lemons_bogof)
        normal_total = self.normal_total(items)
        new_total = adjuster.get_adjusted_price(normal_total, items)
        old_price_for_items = 4 * 1.50
        new_price_for_items = 2 * 1.50
        assert new_total == normal_total - (old_price_for_items - new_price_for_items)
        
    def test_multibuy_discount_across_types(self, items):
        """
        items has 4 lemon at 1.50 and 1 grapefruit at 1.25, so 5.25
        deal captures cheapest 4, leaving one lemon full price
        """
        two_for_a_pound = MultibuyOffer(['lemon', 'grapefruit'], 2, 1)
        adjuster = MultibuyPriceAdjuster()
        adjuster.add_offer(two_for_a_pound)
        normal_total = self.normal_total(items)
        new_total = adjuster.get_adjusted_price(normal_total, items)
        old_price_for_items = 4 * 1.50 + 1.25
        new_price_for_items = 2 * 1 + 1.50
        assert new_total == normal_total - (old_price_for_items - new_price_for_items)
        
        
    
        