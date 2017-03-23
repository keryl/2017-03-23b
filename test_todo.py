import unittest
import todo

class TodoTestCase(unittest.TestCase):

    def test_it_initializes_a_list_attribute(self):
        td = todo.Todo()
        self.assertEqual([], td.tasks)

    def test_add_method_adds_task_string_to_task_array(self):
        td = todo.Todo()
        self.assertEqual([], td.tasks)
        td.add("create repository")
        self.assertEqual(["create repository"], td.tasks)

    def test_add_method_checks_if_task_already_added(self):
        td = todo.Todo()
        self.assertEqual([], td.tasks)

        result = td.add("create repository")
        self.assertEqual(None, result) # check that error was not returned
        self.assertEqual(["create repository"], td.tasks) # check that tasks was added to list

        result = td.add("create repository")
        self.assertEqual("task already exists", result) # error should have been returned
        self.assertEqual(["create repository"], td.tasks) # check that duplicate task was not added

    def test_remove_method_removes_task_from_array(self):

        # create todos object
        td = todo.Todo()
        # ensure its tasks attribute is empty
        self.assertEqual([], td.tasks)

        # add a task
        td.tasks.append("create repository")
        # ensure task is in list
        self.assertEqual(["create repository"], td.tasks)

        # try remove the task
        td.remove("create repository")
        # task should have been removed
        self.assertEqual([], td.tasks)

    def test_remove_method_should_return_error_if_product_not_added(self):
        td = todo.Todo()
        error = td.remove("create repository")
        self.assertEqual("task was not added", error)

if __name__=="__main__":
    unittest.main()