from node import Node

class Tree :

    def __init__(self):
        self.root = None


    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.root.insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def print_result(self):
        self.root.print_result()

