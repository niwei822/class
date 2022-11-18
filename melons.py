"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder:
    
    order_type = None
    tax = 0.0
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_base_price(self):
        base_price = random.randrange(5, 10)
        now = datetime.datetime.now()
        if now.hour in range(8, 12) and now.weekday() < 5:
            base_price += 4
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.tax == 0.17 and self.qty < 10:
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "government"
    tax = 0.0
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed