class Todo():

    def __init__(self):
        self.tasks = []

    def add(self, task):

        if task in self.tasks: # check if task was added
            return "task already exists" # if added, return error
        else:
            self.tasks.append(task) # otherwise add task to list

    def remove(self, task):

        # check if task exists
        # if not return error
        # if exists, remove task and do not return anything

        if task not in self.tasks:
            return "task was not added"
        else:
            self.tasks.remove(task)



