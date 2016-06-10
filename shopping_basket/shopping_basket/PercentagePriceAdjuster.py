"""
PercentagePriceAdjuster applies a percentage discount above a certain value
"""

class PercentagePriceAdjuster(object):
    """
    Applies a percentage discount above a certain value.
    """
    
    def __init__(self, percentage_discount, min_value=0):
        self._percentage_discount = percentage_discount
        self._min_value = min_value
        
    def get_adjusted_price(self, previous_total, items):
        """
        Returns new total if previous is above minimum.
        """
        if previous_total > self._min_value:
            total = float(previous_total)
            return total - total * self._percentage_discount/100
        return previous_total

