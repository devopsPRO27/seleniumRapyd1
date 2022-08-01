import mysql.connector


class Food:
    def __init__(self, cal, flav, price, name):
        self.cal = cal
        self.flav = flav
        self._price = price
        self.name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if newprice > 0:
            self._price = newprice
        else:
            raise ValueError('maaaan go get some coffee ')


f = Food(122, 'salty', 22, 'mc royal')
f.price = 244
print(f.price)
