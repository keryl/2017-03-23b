class Todo():

    def __init__(self):
        self.tasks = {}

    def add(self, task):
        self.tasks[task] = False

