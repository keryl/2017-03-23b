import unittest
import shopping_list

class ShoppingListTestCase(unittest.TestCase):

    def test_it_initializes_a_dictionary_attribute(self):
        sl = shopping_list.ShoppingList()
        self.assertEqual({}, sl.products)


if __name__ =="__main__":
    unittest.main()

