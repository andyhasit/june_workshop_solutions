import pytest
from logic import * 

class TestPercentagePriceAdjuster:
            
    def test_percentage_normally(self):
        adjuster = PercentagePriceAdjuster(10)
        assert adjuster.get_adjusted_price(25, []) == 22.5
        
    def test_percentage_with_min_value(self):
        adjuster = PercentagePriceAdjuster(10, 10)
        assert adjuster.get_adjusted_price(9.00, []) == 9.00
        assert adjuster.get_adjusted_price(25, []) == 22.5
        