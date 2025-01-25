class Computer:
  def _init_(self):
    self._max_price=10000

  def sell(self):
    print("Selling Price of the Computer is ",self._max_price)

  def setmaxprice(self,price):
    self._max_price=price

comp1=Computer()
comp1.sell()

comp1._max_price=20000
comp1.sell()

comp.setmaxprice(20000)
comp1.sell()
