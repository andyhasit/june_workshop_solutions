import pytest
from logic import * 

class TestController:
    
    def test_new_product(self):
        c = Controller()
        c.new_product('apple', 1.50)
        c.new_product('orange', 1.50)
        products = c.get_products() 
        assert len(products) == 2
        
    def test_new_product_with_same_descrition_raises_exception(self):
        c = Controller()
        c.new_product('apple', 1.50)
        with pytest.raises(ValueError):
            c.new_product('apple', 5.50)