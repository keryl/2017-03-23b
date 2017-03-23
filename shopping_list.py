class ShoppingList():

    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product] = False
        
    def bought(self, product):
        self.products[product] = True