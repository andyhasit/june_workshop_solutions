
class DemoHelper(object):
    """
    Helps print basket to the terminal.
    """
    def __init__(self, basket):
        self._table_columns = ('item', 'qty', 'unit', 'total')
        self._padding_values = (20, 8, 8, 8)
        self._basket = basket
    
    def print_basket(self, message):
        self._print_line()
        self._print_line()
        print ""
        print message
        print ""
        self._print_table_header()
        self._print_line()
        for item in self._basket.items:
            self._print_table_row(item)
        print ""
        print 'Gross:  {0}'.format(self._format_currency(self._basket.gross_total))
        print 'Net:    {0}'.format(self._format_currency(self._basket.net_total))
        print ""
        
    def _print_line(self):
        print "-------------------------------------------------------"
        
    def _print_table_row(self, item):
        description = item.description
        quantity = str(item.quantity)
        unit_price = self._format_currency(item.unit_price)
        total = self._format_currency(item.total)
        fields = (description, quantity, unit_price, total)
        print self._pretty_table_line(fields)
    
    def _format_currency(self, value):
        return '{:,.2f}'.format(value)
    
    def _print_table_header(self):
        print self._pretty_table_line(self._table_columns)
    
    def _pretty_table_line(self, items):
        """
        Pretty prints a line to terminal making it look like a table.
        Just for demo purposes, not safe for real use.
        """
        padded_strings = []
        for i, s in enumerate(items):
            padding_value = self._padding_values[i]
            padded_strings.append('{:<{}s}'.format(str(s), padding_value))
        return "  " + "|   ".join(padded_strings)