from beverage_class import *

boisson = Coffee('choco', '5 min', ['choco'], 'hot', 'juice', 0)
boisson2 = Beverage('choco', '5 min', ['choco'], 'hot', 'juice', 0)
print(boisson.get_all('name', 'type'))
boisson.show()
print(boisson2.get_all('name', 'type'))