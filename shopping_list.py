class ShoppingList():

    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product] = False

    def bought(self, product):

        # check if product was added
        # if not return error
        # if already added, mark product as bought and do not return anything

        product_is_added = self.products.get(product, None)
        if product_is_added == None:
            return "Add product first"

        self.products[product] = True