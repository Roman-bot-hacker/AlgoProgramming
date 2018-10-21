from stack import Stack


class DFS:
    marked = set()
    post = Stack()

    def depth_first_order(self, graph):
        for i in graph:
            if i not in self.marked:
                self.dfs(graph, i)
                self.marked.add(i)
                self.post.push(i)

    def dfs(self, graph, i):
        for j in graph.get(i):
            if (graph.get(j) is not None) and (j not in self.marked):
                self.dfs(graph, j)
            if j not in self.marked:
                self.post.push(j)
                self.marked.add(j)



    def get_reverse_post(self):
        return list(reversed(self.post.items))
