import unittest
import todo

class TodoTestCase(unittest.TestCase):

    def test_it_initializes_a_list_attribute(self):
        td = todo.Todo()
        self.assertEqual([], td.tasks)

    

if __name__=="__main__":
    unittest.main()