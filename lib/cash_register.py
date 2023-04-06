#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0) :
    self.discount=discount
    self.total = 0
    self.items =[]  
    self.last_transact= 0
    
  def add_item(self,title,price,quantity=1):
    self.last_transact= price*quantity
    self.total+=  self.last_transact
    self.items += [title]*quantity
    
    
  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total -= int(self.total * self.discount/100)
      print(f'After the discount, the total comes to ${self.total}.')
  
  def void_last_transaction(self):
    self.total-=  self.last_transact
    del(self.items[-1])
    


diana=CashRegister(10)
diana.add_item("apple", 0.99,15)
diana.add_item("egg", 0.99)
diana.apply_discount()
diana.void_last_transaction()