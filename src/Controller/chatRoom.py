# Command pattern 
from abc import ABC, abstractmethod

#---------------------------
#  Abstract Command class
#---------------------------
class OrderCurrency(ABC):

    @abstractmethod
    def process(self):
        pass

#---------------------------
#  Concrete Command class
#---------------------------
class BuyCurrency(OrderCurrency):
    def __init__(self, stock):
        self.stock = stock

    def process(self):
        self.stock.buy()

#---------------------------
#  Concrete Command class
#---------------------------
class SellCurrency(OrderCurrency):
    def __init__(self, stock):
        self.stock = stock

    def process(self):
        self.stock.sell()

#---------------------------
#  Receiver class
#---------------------------
class Trade:
    def buy(self):
        print("Currency purchase request posted.")

    def sell(self):
        print("An application for the sale of currency has been posted.")

class Invoker:
    def __init__(self):
        self._queue = []

    def process_order(self, order):
        self._queue.append(order)
        order.process()

trade = Trade()
buy_currency = BuyCurrency(trade)
sell_currency = SellCurrency(trade)

invoker = Invoker()
invoker.process_order(buy_currency)
invoker.process_order(sell_currency)
