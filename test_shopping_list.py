import unittest
import shopping_list

class ShoppingListTestCase(unittest.TestCase):

    def test_it_initializes_a_dictionary_attribute(self):
        sl = shopping_list.ShoppingList()
        self.assertEqual({}, sl.products)

    def test_add_method_adds_product_to_products_attribute(self):
        sl = shopping_list.ShoppingList()
        self.assertEqual({}, sl.products)
        sl.add("sugar")
        self.assertEqual({"sugar": False}, sl.products)

    def test_bought_method_marks_product_as_bought(self):
        sl = shopping_list.ShoppingList()
        self.assertEqual({}, sl.products)
        sl.add("sugar")
        sl.bought("sugar")
        self.assertEqual({"sugar": True}, sl.products)


if __name__ =="__main__":
    unittest.main()
