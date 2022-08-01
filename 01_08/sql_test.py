import mysql.connector


class Food:
    def __init__(self, cal, flav, price, name):
        self.cal=cal
        self.flav =flav
        self.price =price
        self.name =name
    

f = Food(122, 'salty', 22, 'mc royal')
f.cal = 122


def s():
    x=32
    
    