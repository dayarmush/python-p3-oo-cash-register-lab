#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = list()
        self.latest = 0

    def add_item(self, title, price, quantity=1):
        self.latest = price * quantity
        self.total += (price * quantity)
        self.items.extend([title] * quantity)
        return self.total
    
    def apply_discount(self):
        if self.discount:
            discount = self.discount/100 * self.total
            self.total -= discount
            return print(f'After the discount, the total comes to ${int(self.total)}.')
        else:
            return print("There is no discount to apply.")
        
    def void_last_transaction(self):
        self.total -= self.latest

        
     
