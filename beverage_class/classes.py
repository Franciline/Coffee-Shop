"""
This file contains the parent class Beverage and the child classes Coffee, Mocktail
"""

class Beverage():
    def __init__(self, name, time, ingred_list, temp, category, available, type = None):
        """
        name, time, temp, category, type: String
        ingred_list: list String
        int: available (0 False 1 True)
        """
        
        self.name = name
        self.time = time
        self.ingred_list = ingred_list
        self.temp = temp
        self.category= category
        self.available = available
        self.type = type

        
    #setters    
    def set_name(self, name):
        """set the variable name"""
        self.name = name

    def set_name(self, time):
        """set the variable time"""
        self.time = time

    def set_name(self, ingred_list):
        """set the variable ingred_list"""
        self.ingred_list = ingred_list

    def set_name(self, temp):
        """set the variable temp"""
        self.temp = temp

    def set_name(self, category):
        """set the variable category"""
        self.category = category

    def set_name(self, available):
        """set the variable available"""
        self.available = available

    #getters
    def get_all(self, *attrib):
        '''Return the selected attributes of the drink, if no arguments passed, return all attributes'''
        dico = vars(self)
        if not attrib: #no attribute selected
            return list(dico.values())
        return [dico[attribute] for attribute in attrib if attribute in dico]

class Coffee(Beverage):
    def __init__(self, name, time, ingred_list, temp, category, available):
        super().__init__(name, time, ingred_list, temp, category, available, 'Coffee')


class Mocktail(Beverage):
    def __init__(self, name, time, ingred_list, temp, category, available):
        super().__init__(name, time, ingred_list, temp, category, available, 'Moctkail')


