import pytest
from logic import * 

class TestBasicBasket:
        
    def test_add_one_item(self):
        apple = Product('apple', 2)
        orange = Product('orange', 2.50)
        basket = BasicBasket()
        basket.add_item(apple, 4)
        items = basket.items
        assert len(items) == 1
        item = items[0]
        assert item.description == 'apple'
        assert item.quantity == 4
        
    def test_add_two_different_items(self):
        apple = Product('apple', 2)
        orange = Product('orange', 2.50)
        basket = BasicBasket()
        basket.add_item(apple, 4)
        basket.add_item(orange, 6)
        items = basket.items
        assert len(items) == 2
        item = items[0]
        assert item.description == 'apple'
        assert item.quantity == 4
        item = items[1]
        assert item.description == 'orange'
        assert item.quantity == 6
        
    def test_add_two_same_items_increments_quantity(self):
        apple = Product('apple', 2)
        orange = Product('orange', 2.50)
        basket = BasicBasket()
        basket.add_item(apple, 4)
        basket.add_item(orange, 6)
        basket.add_item(apple, 6)
        items = basket.items
        assert len(items) == 2
        item = items[0]
        assert item.description == 'apple'
        assert item.quantity == 10
        item = items[1]
        assert item.description == 'orange'
        assert item.quantity == 6
        
    def test_total(self):
        apple = Product('apple', 2)
        orange = Product('orange', 2.50)
        basket = BasicBasket()
        basket.add_item(apple, 4)   # price: 8
        basket.add_item(orange, 2)  # price: 5
        basket.add_item(apple, 2)   # price: 4
        assert basket.total == 8 + 5 + 4
        
        