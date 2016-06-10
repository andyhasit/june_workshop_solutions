from logic import *

class TestItemInBasket():
    
    def test_total(self):
        apple = Product('apple', 1.5)
        item_in_basket = ItemInBasket(apple, 2)
        assert item_in_basket.total == 1.5 * 2
        item_in_basket.update_quantity(3)
        assert item_in_basket.total == 1.5 * 3