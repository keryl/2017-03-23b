import unittest
import todo

class TodoTestCase(unittest.TestCase):

    def test_it_initializes_a_list_attribute(self):
        td = todo.Todo()
        self.assertEqual({}, td.tasks)

    def test_add_method_adds_task_string_to_task_array(self):
        td = todo.Todo()
        self.assertEqual({}, td.tasks)
        td.add("create repository")
        self.assertEqual({"create repository": False}, td.tasks)

if __name__=="__main__":
    unittest.main()