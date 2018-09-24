class Node :
    def __init__(self, data, par = None):
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.data)
        return 'Root : ' + str(self.data)

    def is_leaf(self):
        return len(self.child) == 0

    def insert(self, new_node):
        if self.is_leaf():
            self.add(new_node)

        elif new_node.data[0] > self.data[-1]:
            self.child[-1].insert(new_node)

        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i].insert(new_node)
                    break


    def add(self, new_node):
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort(key=lambda child: child.data[0])
            for child in self.child:
                child.parent = self
        if len(self.data) > 2:
            self.split()


    def split(self):
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]
        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent.add(self)

        else:
            left_child.parent = self
            right_child.parent = self


    def print_result(self):
        print(' | ' + str(self.parent) + ' : ' + str(self.data) + ' | ')
        for child in self.child:
            child.print_result()